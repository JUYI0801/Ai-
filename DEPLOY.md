# 部署指南

## 步骤1：在GitHub上创建仓库

1. 访问 https://github.com/new
2. 填写仓库名称（例如：ai-model-comparison-2026）
3. 选择 Public 或 Private
4. **不要**勾选 "Initialize this repository with a README"
5. 点击 "Create repository"

## 步骤2：推送代码到GitHub

在本地项目目录下执行以下命令：

```bash
# 添加所有文件
git add .

# 初次提交
git commit -m "Initial commit"

# 重命名分支为main（如果需要）
git branch -M main

# 添加远程仓库（替换为你的用户名和仓库名）
git remote add origin https://github.com/[你的用户名]/[仓库名].git

# 推送到GitHub
git push -u origin main
```

## 步骤3：启用GitHub Pages

1. 进入你的GitHub仓库
2. 点击 "Settings" 标签
3. 在左侧菜单中找到 "Pages"（在 "Code and automation" 部分）
4. 在 "Build and deployment" 下：
   - Source: 选择 "Deploy from a branch"
   - Branch: 选择 "main" 分支，文件夹选择 "/ (root)"
5. 点击 "Save"
6. 等待几分钟，页面将自动部署

## 步骤4：获取访问地址

部署完成后，你的网页可以通过以下地址访问：
`https://[你的GitHub用户名].github.io/[仓库名称]/`

## 步骤5：配置自动更新（可选）

自动更新工作流已经配置好了：

- **定时更新**：每周一、三、五 UTC 00:00 自动运行
- **手动触发**：进入仓库的 "Actions" 标签 → 选择 "Auto Update Data" → 点击 "Run workflow"

注意：首次推送后，GitHub Actions可能需要手动启用：
1. 进入仓库的 "Settings" 标签
2. 在左侧菜单找到 "Actions" → "General"
3. 在 "Actions permissions" 下选择 "Allow all actions and reusable workflows"
4. 点击 "Save"

## 自定义数据更新

如果你想实现真正的数据自动更新（从API或数据源获取），可以修改 `update_data.py` 文件，添加数据获取和HTML内容更新的逻辑。
