# 蓝鲸SaaS开发实训课程-前端

## 一、概述

基于蓝鲸SaaS开发框架开发一个独立SaaS应用

- 借助蓝鲸CMDB配置平台实现游戏业务主机资源拉取与查询，通过蓝鲸网关/ESB组件API联通 CMDB平台实现数据获取，并根据CMDB主机数据结构，设计查询条件与对应接口。
- 借助蓝鲸JOB平台实现游戏业务主机日志备份

- 环境搭建文档：[手把手搭建蓝鲸SaaS开发环境-Windows版](https://doc.weixin.qq.com/doc/w3_AX8A1AafADsgPxqA1eYSNGBaxu1TZ?scode=AJEAIQdfAAonOPTizp)
- 蓝鲸桌面：[蓝鲸桌面](https://ce.bktencent.com/console/)
- 蓝鲸MagicBox组件库：[蓝鲸MagicBox组件文档-Vue2版本](https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/)

## 二、本地开发环境搭建
<font color=red size=6> 所有环境相关文件均已在【软件设计与分析】QQ群中上传 </font>

后端开发环境参考此前的SaaS开发环境搭建文档：[手把手搭建蓝鲸SaaS开发环境-Windows版](https://doc.weixin.qq.com/doc/w3_AX8A1AafADsgPxqA1eYSNGBaxu1TZ?scode=AJEAIQdfAAonOPTizp)

### 环境说明

前端开发环境不做强制限制，实验手册中为基于蓝鲸前端开发框架MagicBox组件库的实现

具体环境为<font color=red size=6>NVM+Node.js v20.10.0+Vue2+MagicBox</font>

NVM安装包：[NVM安装包](https://drive.weixin.qq.com/s?k=AJEAIQdfAAoG1E2mr2)

NVM安装可以参考：[Windows环境下安装NVM进行NodeJS管理](https://www.freecodecamp.org/chinese/news/nvm-for-windows-how-to-download-and-install-node-version-manager-in-windows-10/)

以管理员身份运行，一直下一步即可。

### 本地开发：

首先，需要使用NVM安装node.js v20.10.0，命令如下：

```shell
nvm install v20.10.0
```

![企业微信截图_17131736977270](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_17131736977270.png)

添加前端环境变量配置，在项目根目录下创建`.bk.local.env`文件，并添加以下代码：

```python
BK_LOGIN_URL=https://ce.bktencent.com/login/
BK_APP_HOST='dev.ce.bktencent.com'
BK_AJAX_URL_PREFIX = '/'
BK_USER_INFO_URL = '/user'
```

![image-20240416165356724](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240416165356724.png)

使用IDE打开解压后的前端项目模版，笔者这里使用的是WebStorm作为前端IDE，在IDE终端中切换Node JS版本，并安装前端所需依赖：
<font color=red size=6>切换对应的NPM版本`nvm use 20.10.0`后，在项目根目录下执行 `npm install`安装环境依赖，如下图：</font>

![企业微信截图_17131745456125](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_17131745456125.png)

随后，设置NPM启动配置：

![企业微信截图_17131745818084](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_17131745818084.png)

![image-20240416165530752](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240416165530752.png)

![image-20240416165601681](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240416165601681.png)

访问 http://dev.ce.bktencent.com:5000/，可看到以下界面：

![image-20240416165651014](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240416165651014.png)

## 三、开发样例-实现级联选框，业务->集群->模块联动

对应实验要求一：

![image-20240418145428621](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240418145428621.png)

在这里，我们使用两个前端组件 `bk-form`和`bk-select`，分别对应一个查询表单和各个下拉选框

组件文档（bk-form）：[Form表单组件文档](https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/form)

组件文档（bk-select）：[Select选框组件文档](https://magicbox.bk.tencent.com/static_api/v3/components_vue/2.0/example/index.html#/select)

本步骤完整的页面代码：[L2实验前端代码](https://gitee.com/CHD-EASY-GOING/bk-scut-course-demo-frontend/blob/master/src/views/example1/index.vue)

简单介绍一下蓝鲸前端开发框架的目录结构：

- 在`src/views`下存放我们所有的`VUE`页面组件文件
- 在`router/index.js`下编写路由，新增页面后需要在此进行编写
- 在`store/modules/example.js`下编写JS函数，实现与后端接口联通

![image-20240418150856937](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240418150856937.png)

我们本期实验的所有页面均在`src/views/example1/index.vue`中完成，相应与后端接口的联通则在`store/modules/example.js`中实现。

### 数据定义

同上图，在`example1/index.vue`中的`data()`部分，添加对应部分：

```javascript
data() {
    return {
      size: 'small',
      formData: {
        name: '',
        date: '',
      },
      tableData: [],
      biz_list:  [],  // 业务列表
      set_list:  [],  // 集群列表
      module_list: [],  // 模块列表
      biz_id:null,    // 当前选中的业务ID
      set_id:null,    // 当前选中的集群ID
      module_id:null, // 当权选中的模块ID
      pagination: {
        current: 1,
        count: 0,
        limit: 10,
      },
    };
  },
```

### 表单设计&下拉选框

```vue
<bk-form form-type="inline">
        <bk-form-item label="业务">
          <bk-select
              :disabled="false"
              style="width: 250px;"
              ext-cls="select-custom"
              @change="handleBizChange"
              ext-popover-cls="select-popover-custom"
              searchable>
            <bk-option
                v-for="item in biz_list"
                :key="item.bk_biz_id"
                :id="item.bk_biz_id"
                :name="item.bk_biz_id+'-'+item.bk_biz_name"></bk-option>
          </bk-select>
        </bk-form-item>
        <bk-form-item label="集群">
          <bk-select
              v-model="set_id"
              :disabled="false"
              style="width: 250px;"
              ext-cls="select-custom"
              @change="handleSetChange"
              ext-popover-cls="select-popover-custom"
              searchable>
            <bk-option
                v-for="item in set_list"
                :key="item.bk_set_id"
                :id="item.bk_set_id"
                :name="item.bk_set_id+'-'+item.bk_set_name"></bk-option>
          </bk-select>
        </bk-form-item>
        <bk-form-item label="模块">
          <bk-select
              v-model="module_id"
              :disabled="false"
              style="width: 250px;"
              ext-cls="select-custom"
              @change="handleModuleChange"
              ext-popover-cls="select-popover-custom"
              searchable>
            <bk-option
                v-for="item in module_list"
                :key="item.bk_module_id"
                :id="item.bk_module_id"
                :name="item.bk_module_id+'-'+item.bk_module_name"></bk-option>
          </bk-select>
        </bk-form-item>
        <bk-form-item label="日期">
          <bk-date-picker placeholder="日期" :timer="false" v-model="formData.date" />
        </bk-form-item>
        <bk-form-item>
          <bk-button theme="primary" title="提交">搜索</bk-button>
        </bk-form-item>
      </bk-form>
```

在这里，简单讲一下这里使用的`bk-select`组件，核心是通过bk-option来进行数据绑定与选择，通过`@change=handlexxxChange`来监听变更事件

### 后端接口联通

我们在`store/modules/example.js`中添加JS函数，实现与后端API的联通

```python
		// 查询业务列表
    getBizData(context, params, config = {}) {
      // eslint-disable-next-line no-undef
      return http.get(`http://dev.ce.bktencent.com:8000/biz-list`, params, config);
    },
    // 根据业务ID，查询集群列表
    getSetData(context, params, config = {}) {
      // eslint-disable-next-line no-undef
      const url = `http://dev.ce.bktencent.com:8000/set-list?${queryString.stringify(params)}`;
      return http.get(url, {}, config);
    },
    // 根据业务ID和集群ID，查询模块列表
    getModuleData(context, params, config = {}) {
      // eslint-disable-next-line no-undef
      const url = `http://dev.ce.bktencent.com:8000/module-list?${queryString.stringify(params)}`;
      return http.get(url, {}, config);
    },
```

![image-20240418153046702](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240418153046702.png)

### 页面初始化时，加载业务列表至业务下拉选框

```javascript
created() {
    this.init();		// 通过created()勾子函数，执行初始化操作
  },

init() {
      // 页面初始化时执行
      this.getBizData();
    },

async getBizData() {
      try {
        // 初始化业务列表数据，渲染至select下拉选框
        const res = await this.$store.dispatch('example/getBizData', {}, { fromCache: true });
        this.biz_list=res.data.info
      } catch (e) {
        console.error(e);
      }
    },
```

### 变更事件监听&联动查询

```javascript
		async handleBizChange(newValue, oldValue) {
      console.log('切换了业务，业务ID为：',newValue)
      this.biz_id = newValue
      this.set_id = null    // 每次切换业务ID后，需要重置此前的集群ID和模块ID
      this.module_id = null


      const set_res = await this.$store.dispatch('example/getSetData',{"bk_biz_id":newValue},{fromCache:true})
      this.set_list = set_res.data.info
    },
    async handleSetChange(newValue, oldValue) {
      // 点击集群ID后，查询集群下所有模块，并回显至对应组件
      console.log('切换了集群，集群ID为：',newValue)
      this.set_id = newValue
      this.module_id = null   // 切换集群后，需要重置此前的模块ID
      const module_res = await this.$store.dispatch('example/getModuleData',{"bk_biz_id":this.biz_id,"bk_set_id":this.set_id},{fromCache:true})
      this.module_list = module_res.data.info
    },
    async handleModuleChange(newValue, oldValue) {
      // 点击集群ID后，查询集群下所有模块，并回显至对应组件
      console.log('切换了模块，模块ID为：',newValue)
      this.module_id = newValue
    },
```

### 实现效果

![image-20240418153339585](https://ctenet-1306582193.cos.ap-nanjing.myqcloud.com/image-20240418153339585.png)