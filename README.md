# 1. 确保在正确的项目目录下
cd /path/to/your/project

# 2. 查看当前所在分支
git branch

# 3. 切换到目标分支（如果不在 main 或 master 分支）
git checkout main  # 或者 git checkout master

# 如果没有 main 分支，可以先创建并切换到 main 分支
git checkout -b main

# 4. 查看新建或修改的文件状态
git status

# 5. 添加所有新建或修改的文件到暂存区
git add .

# 或者只添加特定的文件（可选替代上面的命令）
# git add '文件名'

# 6. 提交这些文件，填写提交信息
git commit -m "描述提交内容的简短信息"

# 7. 设置本地分支与远程仓库分支的关联（首次推送时需要）
git branch -M main  # 确保本地分支为 main
git push -u origin main

# 8. 如果已经设置过关联，可以直接推送到远程仓库的 main 分支
git push origin main
