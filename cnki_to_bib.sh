#!/bin/bash

# 首先从剪切板当中读取数据
string=$(pbpaste)

# 当剪切板中的数据不符合要求时，直接退出脚本
size=${#string}
if [ $size -lt 1 ] && [ $size -gt 200 ]; then
    echo "字符串为空或过长，疑似数据有误！";echo
    exit 1
fi

# 新建函数用以快速切割字符串
# 需要提供原始字符串以及相应的切割符号
# 事实上可以使用cut,sed等高级工具的，但是我不会啊，回头再加以改善吧
function splitString(){
    rawstring=$1
    tempstr=${rawstring//./ }
    arr=($tempstr)
}
# 开始切割字符串
splitString $string .
# 计算数组元素个数
num=${#arr[*]}

if [ $num -ne 3 ] && [ $num -ne 4 ]; then
    echo "剪贴板内数据无法被切割为三组或者是四组，请检查数据";echo
    exit 1
fi


# 开始处理第一组数据，作者的名字以及不需要的[1]
tempstr=${arr[0]}
tempstr=${tempstr#\[*\]}
tempstr=${tempstr//,/ }
temparr=($tempstr)
tempnum=${#temparr[*]}
if [ $tempnum -eq 1 ]; then
    author=$tempstr
else
    for((i=0;i<tempnum;i++))
    do
        if [ $i -eq 0 ]; then
            author=${temparr[$i]}
        else
            author=$author" and "${temparr[$i]}
        fi
    done
fi

# 开始处理第二段数据，去掉最后的[J]直接就可以用啦
tempstr=${arr[1]}
title=${tempstr%\[*\]}

# 开始处理第三段数据
# 首先给出期刊名字

tempstr=${arr[2]}
tempstr=${tempstr//,/ }
temparr=($tempstr)
journal=${temparr[0]}

# 开始抽离出后续的内容
# 首先是页码
tempstr=${temparr[1]}
tempstr=${tempstr//:/ }
temparr=($tempstr)
pages=${temparr[1]}

# 开始抽出期刊时间与相应的卷数
tempstr=${temparr[0]}
tempstr=${tempstr//\(/ }
tempstr=${tempstr//\)/}
temparr=($tempstr)
year=${temparr[0]}
number=${temparr[1]}


# 这里准备输出的模板

# 使用ch2py来输出作者首字母的拼音
# https://blog.csdn.net/hanchaohao2012/article/details/53678319
# sudo gem install chinese_pinyin

key=$(ch2py ${author:0:1})
result="@article{$key$year,\n  \
        author={$author},\n  \
        title={$title},\n  \
        journal={$journal},\n  \
        year={$year},\n  \
        number={$number},\n  \
        pages={$pages},\n  \
        language={chinese},\n\
        }"

# 将最后的结果输出到剪贴板中
echo -e $result | pbcopy
echo "脚本运行完毕，请直接在bib数据库中粘贴数据！"
exit 0
