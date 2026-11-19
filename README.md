# URDF Viewer

用于在浏览器中读取 URDF，并结合 STL 网格进行三维检查。当前工程包含已经验证过的 E05-Pro 示例模型，界面提供：

- STL 三维渲染与 OrbitControls 视角操作
- URDF joint 名称、父子 link、origin、rpy、axis 标注
- 按世界法向轴显示旋转方向：X 红、Y 绿、Z 蓝
- 关节角滑块、连接明细、三维 XYZ 坐标轴和 0.1 m 参考尺
- link/component 可展开列表、悬浮高亮、点击详情和半透明包围盒
- 加载进度统计、固定面板与独立滚动列表
- XYZ（三维传统）/ ZYX（URDF 标准）旋转顺序切换；默认 ZYX
- 点击旋转箭头定位关节，点击三维背景取消选择
- 导入 STL 后按连通三角面自动拆分组件，不改变源文件
- 选择 URDF 文件、选择模型文件夹，或将 URDF/模型文件夹拖入三维区域导入
- 导入时按 URDF 的 link、joint、visual mesh、origin 和 axis 重新构建场景；本地资源通过浏览器内存 URL 读取，不上传文件

## 启动

```bash
cd urdf-viewer
python3 serve.py
```

然后打开：<http://127.0.0.1:8765/>。

也可以运行 `npm start`；项目没有额外的 Node 依赖，Three.js 通过浏览器 import map 从 CDN 加载。

## 模型目录

示例模型位于 `models/e05_pro/`：

- `e05_pro.urdf`：URDF 描述
- `meshes/*.STL`：link 网格
- `meshes/components.json`：组件清单
- `meshes/components/`：组件 STL

导入新的模型时，建议选择包含 URDF 和所有 STL 的模型文件夹；程序会自动寻找 URDF 中声明的 mesh 文件。单独选择 URDF 只能读取描述，若缺少 STL 资源会提示找不到网格文件。浏览器需要通过 HTTP 服务访问，不能直接用 `file://` 打开，否则会被浏览器阻止读取 STL 和 URDF。


## 校验

```bash
node tests/components.cjs
python3 tests/build-browser-check.py
```

启动服务后访问 `/tests/import-check.html` 可执行 E05 导入回归测试。生成的测试页不提交 Git。

## 示例资源与限制

- `models/e05_pro/`：本项目调试使用的华沿 E05-Pro 描述和 STL 资源。
- `models/unitree_g1/`：来自 [Unitree 官方仓库](https://github.com/unitreerobotics/unitree_ros/tree/master/robots/g1_description) 的 G1 29 自由度 URDF 和引用的 36 个 STL；来源记录见 `SOURCE.txt`。第三方资源的权利归各自权利人所有。
- 自动组件编号根据连通块重新生成，可能与预先生成的清单编号不同。
- 当前导入器读取每个 link 的第一个 visual mesh，网格格式为 STL；文件夹拖拽的递归读取尚未实现，请通过“选择模型文件夹”导入完整目录。
- Three.js 需要访问 CDN；选择的文件在浏览器本地读取，不发送给第三方服务。
