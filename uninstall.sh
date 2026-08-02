#!/bin/bash
echo "[i] 正在卸载 Raven-Storm..."
echo "[i] 警告：此操作将永久删除所有备份和数据."
sudo rm -i /usr/bin/rst
sudo rm -rf -i /usr/share/Raven-Storm

echo "[i] RRaven-Storm 卸载完成."
exit 0
