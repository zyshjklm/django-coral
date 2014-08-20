django-coral
============

django-coral使django开发者快速开发的模板。


下划线
*******

细项以圆点标示
* 项目一
* 项目二 

### 小标题
  小标题类似html的<h3>
  小标题的格式如下 ### 小标题
  注意#和标题字符中间要有空格

单行文本框
    这是一个单行的文本框,只要两个Tab或空格再输入文字即可

多行文本框  
    多行不能简单回车这么简单  
    你可以写入代码等,每行文字只要在行首和行尾输入两个Tab或空格即可

如果你要标注一段代码,譬如一段helloworld:
```
    void main(void){
       printf("hello world!");
       return;
    }
```

突出显示
`highlight` 这里被方框突出显示了

链接
1.[点击这里你可以链接到www.google.com](https://github.com/shanhuhai5739/django-coral/blob/master/static/img/logo.png)  
2.[点击这里我你可以链接到我的博客](http://guoyunsky.iteye.com)  

只是显示图片
![github](https://github.com/shanhuhai5739/django-coral/blob/master/static/img/logo.png "github")

想点击某个图片进入一个网页,比如我想点击github的icorn然后再进入www.github.com
[![image]](http://www.github.com/)
[image]: http://github.com/github.png "github"

文字加粗
这里的文字被加粗处理 __BOLD__

表格
|_. ID |_.表名 |
| 1 | 项目1 |
| 2 | 项目2 |

数据流图
{{{{{{ blue-modern
  alice->bob: Test
  bob->alice: Test response
}}}}}}

文字被些字符包围
> 文字被些字符包围
>
> 只要再文字前面加上>空格即可
>
> 如果你要换行的话,新起一行,输入>空格即可,后面不接文字
> 但> 只能放在行首才有效

文字被些字符包围,多重包围
> 文字被些字符包围开始
>
> > 只要再文字前面加上>空格即可
>
>  > > 如果你要换行的话,新起一行,输入>空格即可,后面不接文字

特殊字符处理
有一些特殊字符如<,#等,只要在特殊字符前面加上转义字符\即可
你想换行的话其实可以直接用html标签<br />
