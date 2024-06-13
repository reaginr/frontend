<template>
  <div class="example3-wrapper">
    <bk-container :col="11">
      <bk-col :span="10">
        <bk-form form-type="inline">
          <bk-form-item label="业务">
            <p style="font-size: 14px">demo体验业务</p>
          </bk-form-item>
        </bk-form>
        <br>
        <br>
        <bk-form form-type="inline">
          <bk-form-item label="查询目录">
            <bk-input v-model="searchPath" />
          </bk-form-item>
          <bk-form-item label="查找后缀">
            <bk-input v-model="suffix" />
          </bk-form-item>


          <bk-form-item>
            <span v-bk-tooltips.top-start="'目录以\' / \'开头，后缀不包含\' . \''" style="color: #3b83ff">
              <i class="bk-icon icon-info-circle-shape"></i>
            </span>
          </bk-form-item>

          <bk-form-item label="主机">
            <bk-select
                :disabled="false"
                style="width: 250px;"
                ext-cls="select-custom"
                @change="handleHostChange"
                ext-popover-cls="select-popover-custom"
                searchable>
              <bk-option
                  v-for="item in this.hostList"
                  :key="item.bk_host_id"
                  :id="item.bk_host_id"
                  :name="item.bk_host_id+'-'+item.bk_host_innerip"></bk-option>
            </bk-select>
          </bk-form-item>

          <bk-form-item label="备份目录">
            <bk-input v-model="backupPath" />
          </bk-form-item>
          <bk-form-item>
            <bk-button :theme="'primary'" type="submit" @click="searchFile" class="mr10">查询</bk-button>
          </bk-form-item>
        </bk-form>

        <bk-table
            style="margin-top: 15px;"
            :data="fileData"
            v-bkloading="{ isLoading: isLoading, title: loadingText, zIndex: 15 }">
          <bk-table-column label="主机ID" prop="bk_host_id" />
          <bk-table-column label="文件列表" prop="bk_file_list" />
          <bk-table-column label="文件数量" prop="bk_file_cnt" />
          <bk-table-column label="文件总大小(字节)" prop="bk_file_total_size" />
          <bk-table-column label="操作" prop="bk_file_option">
            <template slot-scope="{ row }">
              <span @click="backupFile(row.bk_host_id)" style="color: #0000edff; cursor: pointer;">立即备份</span>
            </template>
          </bk-table-column>
        </bk-table>
      </bk-col>
    </bk-container>
  </div>
</template>

<script>

export default {
  components: {
  },
  data() {
    return {
      suffix: 'log',
      hostList: [],
      host_id: null,
      host_id_list: [],
      searchPath: '/project',
      backupPath: '/project/backup',
      fileData: [],
      isLoading: false,
      loadingText: '',
    };
  },
  created() {
    this.searchHosts();
  },
  methods: {
    async searchHosts() {
      const data = { bk_biz_id: 3 };
      const hostRes = await this.$store.dispatch('example/getHostsData', data, { fromCache: true });
      // 对可用主机做筛选
      this.hostList = hostRes.data.info
      console.log(this.hostList)
      for (const host of this.hostList) {
        host.is_selected = false;
      }
    },
    async searchFile() {
      this.host_id_list=[this.host_id];
      console.log('host_id_list', this.host_id_list);
      if (this.host_id_list.length === 0) {
        const config = {
          theme: 'primary',
          message: '请选择主机！',
          offsetY: 80,
        };
        this.$bkMessage(config);
        return;
      }
      // TODO: 可修改为更完备的参数校验
      if (this.searchPath === '') {
        const config = {
          theme: 'primary',
          message: '请输入查找目录！',
          offsetY: 80,
        };
        this.$bkMessage(config);
        return;
      }
      if (this.suffix === '') {
        const config = {
          theme: 'primary',
          message: '请输入查找后缀！',
          offsetY: 80,
        };
        this.$bkMessage(config);
        return;
      }
      const queryData = {
        host_id_list: this.host_id_list,
        search_path: this.searchPath,
        suffix: this.suffix,
      };
      this.loadingText = '正在查找文件……';
      this.isLoading = true;
      let res;
      try {
        res = await this.$store.dispatch('example/searchFile', queryData, {});
      } catch (err) {
        console.log(err);
        this.isLoading = false;
        return;
      }
      this.isLoading = false;
      this.fileData = [];
      let errMsg = '';
      for (const log of res.data) {
        if (log.message) {
          // 目录不存在或查找失败
          errMsg += `${log.bk_host_id}: ${log.message}` + '; ';
        } else {
          this.fileData.push(JSON.parse(JSON.stringify(log)));
        }
      }
      if (errMsg !== '') {
        const config = {
          theme: 'error',
          message: errMsg,
          offsetY: 80,
          ellipsisLine: 3,
        };
        this.$bkMessage(config);
      }
    },
    async handleHostChange(newValue, oldValue) {
      console.log('切换了主机，主机ID为：',newValue)
      this.host_id=newValue
    },
    async backupFile(hostId) {
      this.host_id_list = [hostId];
      if (this.backupPath === '') {
        const config = {
          theme: 'primary',
          message: '请输入备份目录！',
          offsetY: 80,
        };
        this.$bkMessage(config);
        return;
      }
      const queryData = {
        host_id_list: this.host_id_list,
        search_path: this.searchPath,
        suffix: this.suffix,
        backup_path: this.backupPath,
      };
      this.loadingText = '正在备份文件……';
      this.isLoading = true;
      try {
        await this.$store.dispatch('example/backupFile', queryData, {});
      } catch (err) {
        console.log(err);
        this.isLoading = false;
        return;
      }
      this.isLoading = false;
      const config = {
        theme: 'success',
        message: '文件备份成功！',
        offsetY: 80,
      };
      this.$bkMessage(config);
    },
  },
};
</script>
