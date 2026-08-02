#!/bin/bash
echo "[i] 现在将 Raven-Storm 安装到您的 bin 路径..."
if [ -d "/usr/share/Raven-Storm" ] ; then
    echo "[i] 发现旧版本 Raven-Storm，正在继续更新..."
    echo "[i] 正在备份旧版本。"
    if [ -d "/usr/share/Raven-Storm/Backup" ] ; then
        sudo mv /usr/share/Raven-Storm/Backup ./Backup
    else
        mkdir ./Backup
    fi
    name="./Backup/Raven-Storm"
    if [ -d $name ] ; then
        i=0
        while [ -d "$name.bak$i" ] ; do
            let i++
        done
            name="$name.bak$i"
    fi
    sudo mv /usr/share/Raven-Storm $name
    mv ./Backup ./Raven-Storm/
    sudo cp -ar ./Raven-Storm /usr/share/
    echo "[i] 安装成功。"
    echo "[i] 正在将 Raven-Storm 设置为可执行文件..."
    sudo mv /usr/share/Raven-Storm/main.py /usr/share/Raven-Storm/rst
    sudo chmod +x /usr/share/Raven-Storm/rst
    sudo ln -s /usr/share/Raven-Storm/rst /usr/bin/rst || echo "[i] 链接似乎已存在。"
else
    sudo cp -ar ./Raven-Storm /usr/share/
    echo "[i] 安装成功。"
    echo "[i] 正在将 Raven-Storm 设置为可执行文件..."
    sudo mv /usr/share/Raven-Storm/main.py /usr/share/Raven-Storm/rst
    sudo chmod +x /usr/share/Raven-Storm/rst
    sudo ln -s /usr/share/Raven-Storm/rst /usr/bin/rst || echo "[i] 链接似乎已存在。"
fi

echo "[i] 现在可以删除 Raven-Storm 文件夹。"
echo "----------------------------------------"
echo "[i] 运行 'sudo rst' 以启动 Raven-Storm。"
echo "----------------------------------------"
exit 0
