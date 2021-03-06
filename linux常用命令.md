【 find 】  
格式：
find      path           -option         [   -print ]   [ -exec   -ok   command ]   {} \  
find      (指定目录)     (指定选项)                     [查找之后执行的动作 ]  
  
#-print 将查找到的文件输出到标准输出  
#-exec   command   {} \;      —–将查到的文件执行command操作,{} 和 \;之间有空格  
#-ok 和-exec相同，只不过在操作前要询用户  
  
常用：  
按照文件名查找：  
find /home  -name "*.t?t"   *表示通配任意个字符  ？表示通配单个字符  
find . | xargs grep string #查找当前目录下文件内容包含字符串string的文件  
（为什么要这样写，因为管道命令符是把上一部的结果传递给下一步来处理，  
在 find . | grep string中虽然看似和find . | xargs grep string差不多，但是实际上还是有区别的。  
find .得到的结果是一串文件名集合，如果直接传递给grep的话，grep会把这些文件名看作一些无意义的字符串来处理。  
但是传递给xargs，他会把他当作一个有意义的文件来处理。）  
(xargs会将管道命令符|前面的内容，当做参数传入后面的命令，这样grep找的就是参数代表的文件，  
而没有args的话，会将|前面的输出内容，  
因此find . -name "aa*" |  grep  hello  找不到文件名包含hello的，因此输出为空，  
find . -name "aa*" | xargs grep  么 -ls   则输出的是文件内容包含“么”的文件  
find . -name "aa*" | xargs grep hello  -ls 则输出的是文件内容 包含“hello”的aa.json文件。)  
按照更新时间查找：  
              -cmin 单位是分
find   /usr   -mtime  -4   查找文件更新日时在距现在时刻4天以内的文件  
find   /usr  -mtime  +4    查找文件更新日时在距现在时刻5天以上的文件  
find   /usr   -mtime   4   查找文件更新日时在距现在时刻4天以上5天以内的文件  
按照所属人查找：  
find ./ -user lzj 查找所有者为lzj的文件或目录  
find ./ -group gname 查找组名为gname的文件或目录  
find ./ -nouser 查找文件的用户ID不存在的文件  
find ./ -nogroup 查找文件的组ID不存在的文件  
find / -nouser  -a -nogroup  可以找出系统中不属于任何人和任何群组的文件，对于这些文件我们需要保持警惕。  
这里我们可以引申 -a -o -not的用法：  
-o 是或者的意思  
-a 是而且的意思  
-not 是相反的意思  
按照文件类型来查找文件：  
find / -type p 查找管道类型的文件  
按照文件大小查找：  
 find  / -size  +10M 列出/usr中大于10M的文件  
  
  
【 grep 】  
linux 查找含有某字符串的所有文件  
grep -r "{关键字}"  {路径}  
如果你想在当前目录下查找"hello,world!"字符串,可以这样:  
grep -nr "hello,world!" *  
* : 表示当前目录所有文件，也可以是某个文件名  
-r 是递归查找  
-n 是显示行号  
-R 查找所有文件包含子目录  
-i 忽略大小写  
  
  
【 ls 】  
ls [-alrtAFR] [name...]  
-a 显示所有文件及目录 (ls内定将文件名或目录名称开头为"."的视为隐藏档，不会列出)  
-l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出  
-r 将文件以相反次序显示(原定依英文字母次序)  
-t 将文件依建立时间之先后次序列出  
-A 同 -a ，但不列出 “.” (目前目录) 及 “…” (父目录)  
-F 在列出的文件名称后加一符号；例如可执行档则加 “*”, 目录则加 “/”  
-R 递归列出全部的目录内容 recusive  
-S 按照文件大小，大的在前面  
  
常用：  
ls -l |grep "^-"|wc -l 或者 ls |wc -l  统计某文件夹下文件的个数  
ls -l |grep "^ｄ"|wc -l   统计某文件夹下目录的个数  
ls -lR|grep "^-"|wc -l   统计文件夹下文件的个数，包括子文件夹里的  
wc -l 统计输出信息的行数，由于一行信息对应一个文件，所以也就是文件的个数。  
