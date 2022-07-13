<template>
        <el-container>
  <el-aside width="200px" class="managerAside">
      <img src="../assets/th2.png" alt="" class="logo"/>
      <div class="gl2">
          <el-dropdown>
               <span class="el-dropdown-link">
            用户管理<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
      <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="back()">首页</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
      </div>
      <div class="gl">
      <el-dropdown>
               <span class="el-dropdown-link">
            团队成员<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
      <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>项目经理：解世超</el-dropdown-item>
          <el-dropdown-item>服务端工程师：何毅</el-dropdown-item>
          <el-dropdown-item>服务端工程师：江顺</el-dropdown-item>
          <el-dropdown-item>客户端工程师：陈泽锋</el-dropdown-item>
          <el-dropdown-item>客户端工程师：蒋涵</el-dropdown-item>
          <el-dropdown-item>数据库工程师：贺思超</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
      </div>
  </el-aside>
  <el-container>
    <el-header class="managerHead">
        <i class="el-icon-help">航班延误预测系统</i>
        <div>
            <el-dropdown>
               <span class="el-dropdown-link">
            个人中心</span>
      <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="exits">退出</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
        </div>
    </el-header>
    <el-main class="managerMain">
         <!--面包屑导航区域-->
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/MAIN-INTER' }" class="head-bread">首页</el-breadcrumb-item>
            <el-breadcrumb-item class="head-bread">用户管理</el-breadcrumb-item>
            <el-breadcrumb-item class="head-bread">用户列表</el-breadcrumb-item>
        </el-breadcrumb>
        <el-card class="box-card">
            <el-row :gutter="20">
        <!-- 搜索 clearable:清空数据，@clear:查询数据-->
        <el-col :span="8">
          <el-input
            placeholder="请输入内容"
            v-model="queryInfo.query"
            clearable
            @clear="getUserList"
          >
            <el-button
              slot="append"
              icon="el-icon-search"
              @click="getUserList"
            ></el-button> </el-input
        ></el-col>
        <!-- 添加用户 -->
        <el-col :span="4"
          ><el-button type="primary" @click="addDialogVisible = true"
            >添加用户</el-button
          >
          <!-- 添加用户对话框 -->
          <el-dialog
            title="添加用户"
            :visible.sync="addDialogVisible"
            width="50%"
            @close="addDialogClosed"
          >
            <!-- 添加用户内容主体区域 -->
            <el-form
              v-model="addUserForm"
              v-rules="addUserFormRules"
              ref="addUserFormRef"
              label-width="70px"
            >
              <el-form-item label="用户名" prop="username">
                <el-input v-model="addUserForm.username"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input v-model="addUserForm.password"></el-input>
              </el-form-item>
             </el-form>
            <!-- 添加用户内容底部区域 -->
            <span slot="footer" class="dialog-footer">
              <el-button @click="addDialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="addUser">确 定</el-button>
            </span>
          </el-dialog>
        </el-col></el-row>
            <el-table :data="userList" border stripe style="position:relative">
        <el-table-column type="index"></el-table-column>
        <el-tableColumn label="姓名" prop="username"></el-tableColumn>
        <el-tableColumn label="操作" width="180px">
          <!-- eslint-disable-next-line -->
          <template slot-scope="scope">

            <!-- 删除用户按钮 -->
            <el-button
              type="danger"
              icon="el-icon-delete"
              size="mini"
              @click="removeUserById(scope.row.username)"
            ></el-button>
            </template></el-tableColumn>
      </el-table>
        </el-card>
    </el-main>
      <el-footer class="managerFoot">
          <div class="kaifa">国寄纵队小组开发出品</div>
      </el-footer>
  </el-container>
</el-container>
</template>

<script>
    export default {
        name: "Manager",
        data() {
            return {
                queryInfo: {
                query: '',
              },
                 // 获取用户列表数据,存放到userList中,查询条数放到total中
                userList: [],
                
                addUserForm: {
                username: '',
                password: '',
              },
                 addUserFormRules: {
                    username: [
                  { required: true, message: '请输入合法的用户名', trigger: 'blur' },
                  {
                    min: 1,
                    max: 10,
                    message: '用户名的长度在3-10个字符之间',
                    trigger: 'blur',
                  },
                ],
                password: [
                  { required: true, message: '请输入合法的密码', trigger: 'blur' },
                  {
                    trigger: 'blur',
                  },
                ],

                 },
                addDialogVisible: false,
            }
        },
        created() {
                    this.getUserList();
                  },
        methods: {
            exits(){
                this.$router.push({path: '/'})
            },
            addDialogClosed() {
                this.$refs.addUserFormRef.resetFields()
            },
            back(){
                this.$router.push({path: 'MAIN-INTER'})
            },
            addUser() {

                    this.axios.post('http://localhost:5000/signup',this.addUserForm).then((resp) =>{
                    let data = resp.data;
                    if(data.toString()=="true"){
                this.$message({
                    message: '添加成功',
                    type: 'success'
                });

                    // 隐藏添加用户的对话框
                    this.addDialogVisible = false
                    // 重新获取用户列表
                    this.getUserList()
                    }else{
                        this.$message.error('添加失败');
                    }
                })
                  },
            async getUserList() {

                let that = this;
                    this.axios.get('http://localhost:5000/listUser').then(function (res) {
                        that.userList = res.data.users;
                  })
                     },
            // 根据Id删除用户
            async removeUserById(username) {
              const confirmRes = await this.$confirm(
                '此操作将永久删除该用户, 是否继续?',
                '提示',
                {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning',
                }
              ).catch((err) => err)
              // 如果用户确认删除，返回confirm
              // 如果用户取消删除，返回cancel
              if (confirmRes !== 'confirm') {
                return this.$message.info('已取消删除')
              }
              console.log(username)
                const deleteForm = {username: username};
                this.axios.post('http://localhost:5000/deleteuser',deleteForm).then((res)=>{
                  let data = res.data;
                  if(data.toString()=="true"){
                      this.$message.success('删除用户成功！')
                      this.getUserList()
                  }else{
                      this.$message.success('删除用户失败')
                  }
              })
            },


        }
    }
</script>

<style scoped>
     .head-bread{
        position: relative;
         color: #fff;
         font-size: 20px;
         line-height:1.7;
    }
     .el-dropdown-link {
        cursor: pointer;
        color: #fff;
         font-size: 30px;
         line-height:1.7;
      }
      .el-icon-arrow-down {
        font-size: 30px;
      }
     .gl{
        text-align: center;
    }
    .gl2{
        text-align: center;
    }
    .logo{
        max-width:100%;
        height:auto;
    }
    .kaifa{
        margin:0px auto 40px auto;
        text-align: center;
        font-size: 20px;
        line-height:60px;
        color: #fff;
        font-family: "Helvetica Neue";
    }
    .el-icon-help{
        text-align: center;
        font-size: 35px;
        color: #fff;
        font-family: "Helvetica Neue";
        line-height:1.7;
    }
    .managerHead{
        background: #409EFF;
        display: flex;
        justify-content: space-between;
    }
    .managerAside{
        width: 1000px;
        background: #4169E1;
    }
    .managerMain{
        background: #87CEFA;
        height:800px;
        flex-grow:1;
        background-image: url("../assets/bg.jpg");
        background-size:cover;
        background-repeat: no-repeat;
    }
    .managerFoot{
        background: #409EFF;
    }

</style>