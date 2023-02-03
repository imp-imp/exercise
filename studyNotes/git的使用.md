# git的使用

### 1 下载git

### 2 配置git

    git config --global user.name "随便起"
    git config --global user.email "自己的邮箱，也可以是仓库的邮箱"

### 3 初始化仓库

     git init

![image](https://static.dingtalk.com/media/lQDPM5teqbD2IIDNAk7NBP6wvnBu8Oshm00D0mHmKIA5AA_1278_590.jpg)

### 4 检测可用的仓库

    git statu

![image](https://static.dingtalk.com/media/lQDPM5kz3yn3vgDNAk7NBP6wmGdlH6GHf2UD0mH2pcA5AA_1278_590.jpg)

### 5 将文件上传仓库

（git上传文件分为   暂存  未修改   已修改）

（暂存文件上传后变为未修改 ，也就是上传到了git仓库中。修改文件后变为已修改，同时已修改的文件也就变成暂存，因为修改后的文件并未上传仓库且与仓库中的文件内容不一致，需要重新上传）

#### 5.1 刚创建文件时属于未跟踪，git add 是将未跟踪的文件变为跟踪文件，也就是暂存

    git add  *//将全部文件变为暂存
    git add <文件名>  //单独暂存的文件

#### 5.2 将暂存的文件上传仓库

    git commit -m "文件上传时备注的信息"
    git commit -a -m "同上" //-a 提交所以已修改的文件

#### 5.3 如果修改本地文件并且与上传仓库的文件不一致时，需要再次执行5.1和5.2步骤。也可以直接使用5.2中第二个命令，直接进行上传（包含了add和commit）  一步从暂存到未修改。

###  6 git常用命令

####  6.1 还原文件

    git restore <文件名> //还原成上一次未修改的状态
    git restore *  //所以文件还原成上一次未修改的状态
    git restore --staged <文件名> //把删除的文件从暂存状态给还原（取消掉），但还需要上传 并不能恢复操作 也可以用restore还原

#### 6.2 删除文件

    git rm <文件名> //未修改状态时才可以删除，但是会进入暂存，需要commit上传。但如果文件处于已修改状态则无法删除
    git rm <文件名> -f //强制删除，同样也是会进去暂存，需要上传

#### 6.3 移动文件

    git mv <文件名> <修改后的文件名> //把文件的名字修改 还需要上

### 7 分支

    git branch //查看分支
    git branch <分支名> //创建分支
    git branch -d <分支名> //删除分支
    git switch <分支名> //切换分支
    git switch -c <文件名> //创建并切换分支

### 8 变基

在开发中除了通过merge来合并分支外，还可以通过变基来完成分支的合并。

我们通过merge合并分支时，在提交记录中会将所有的分支创建和分支合并的过程全部都显示出来，这样当项目比较复杂，开发过程比较波折时，我必须要反复的创建、合并、删除分支。这样一来将会使得我们代码的提交记录变得极为混乱。

原理（变基时发生了什么）：

1. 当我们发起变基时，git会首先找到两条分支的最近的共同祖先
2. 对比当前分支相对于祖先的历史提交，并且将它们提取出来存储到一个临时文件中
3. 将当前部分指向目标的基底
4. 以当前基底开始，重新执行历史操作

变基和merge对于合并分支来说最终的结果是一样的！但是变基会使得代码的提交记录更整洁更清晰！注意！大部分情况下合并和变基是可以互换的，但是如果分支已经提交给了远程仓库，那么这时尽量不要变基。

### 9 创建本地库并链接远程库流程

将本地库上传git：

```bash
git init #初始化仓库
#创建文件
git add <文件名> #把文件添加到暂存状态
git commit -m "xxxx" #将暂存的文件存储到仓库中 xxxx为备注信息
git remote add origin <远程库地址> # git remote add <remote name> <url>
git branch -M main #修改分支名
git push -u origin main # git push 将代码上传服务器上
```

将本地库上传gitee：

```bash
git remote add gitee 自己仓库地址
git push -u gitee main
```

克隆远程库

```bash
git clone <克隆远程库的地址>
```

多端操作 上传代码时如果本地库与远程库版本不同需要先拉取代码再上传

```bash
git git fetch # 要想推送成功，必须先确保本地库和远程库的版本一致，fetch它会从远程仓库下载所有代码，但是它不会将代码和当前分支自动合并
		 # 使用fetch拉取代码后，必须要手动对代码进行合并
git pull  # 从服务器上拉取代码并自动合并 
```

### 远程库的操作的命令

```bash
git remote # 列出当前的关联的远程库
git remote add <远程库名> <url> # 关联远程仓库
git remote remove <远程库名>  # 删除远程库
git push -u <远程库名> <分支名> # 向远程库推送代码，并和当前分支关联
git push <远程库> <本地分支>:<远程分支>
git clone <url> # 从远程库下载代码
```

