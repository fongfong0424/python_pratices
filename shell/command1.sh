#!/bin/bash
#指定解析器


echo "谢谢大家来参加我本年度的第二次分享"

#新建文件
touch tess.txt

#删除文件
rm tess.txt

#查看当前路径
pwd

#查看目录信息
ls -l

#查看文件
cat
tail
more
less


#统计文件内容信息  行、单词数、字节数
wc -l
wc -w
wc -b


#输出重定向
>
>>

#command1 | command2 |command3

echo "hello" > tess.txt

#定时任务   查看、删除、编辑
crontab -l
