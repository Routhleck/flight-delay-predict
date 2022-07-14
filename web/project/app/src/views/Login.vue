<template>
        <el-container>
  <el-aside width="200px" class="loginAside">
      <img src="../assets/th2.png" alt="" class="logo"/>
      <div class="gl">
      <el-dropdown>
               <span class="el-dropdown-link">
            前往注册<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item @click.native="toLogin()">登录</el-dropdown-item>
        <el-dropdown-item @click.native="toRegister()">注册</el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
      </div>
      <div class="gl2">
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
          <el-dropdown-item>
              <el-link type="primary" href="https://github.com/Routhleck/flight-delay-predict">项目开源地址（仅供学习交流）
              </el-link>
          </el-dropdown-item>
  </el-dropdown-menu>
</el-dropdown>
      </div>
  </el-aside>
  <el-container>
    <el-header class="loginHead">
        <i class="el-icon-help">航班延误预测系统</i>
    </el-header>
    <el-main class="loginMain">
        <el-form ref="loginform" :model="loginForm" class="loginContainer">
            <h3 class="loginTitle">系统登录</h3>
            <el-form-item label="">
                <el-input type="text"
                          auto-complete="false"
                          v-model="loginForm.username"
                          placeholder="请输入用户名"
                          prefix-icon="el-icon-user-solid"></el-input>
            </el-form-item>
            <el-form-item label="">
                <el-input type="password"
                          auto-complete="false"
                          v-model="loginForm.password"
                          placeholder="请输入密码"
                          prefix-icon="el-icon-key"></el-input>
            </el-form-item>
            <el-form-item>
            <el-button type="primary" style="width: 100%" v-on:click="login()">登录</el-button>
            </el-form-item>
             </el-form>
    </el-main>
      <el-footer class="loginFoot">
          <div class="kaifa">国寄纵队小组开发出品</div>
      </el-footer>
  </el-container>
</el-container>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                loginForm: {
                    username: '20301038',
                    password: '123456'
                }
            }
        },
        methods: {
            login() {

                this.axios.post('http://localhost:5000/login',this.loginForm).then((resp) =>{
                    let data = resp.data;
                    if(data.toString()=="true"){
                this.$message({
                    message: '登录成功',
                    type: 'success'
                });
                // this.$router.push({name: 'MAIN-INTER',params:{user_name:this.loginForm.username}})
                this.$router.push({path: '/MAIN-INTER',query:{username:this.loginForm.username}})
                    }else{
                        this.$message.error('登录失败');
                    }
                })

            },
            toRegister() {
                this.$router.push({path: '/Register'})
            },
            toLogin() {
                this.$router.push({path: '/'})
            },
        }
    }
</script>

<style scoped>
    .loginContainer{
        border-radius: 15px;
        background-clip: padding-box;
        margin: 180px auto;
        width: 350px;
        padding: 15px 35px 15px 35px;
        background: #fff;
        border: 1px solid #eaeaea;
        box-shadow: 0 0 25px #cac6c6;
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
        margin:0px auto 40px auto;
        text-align: center;
        font-size: 35px;
        color: #fff;
        font-family: "Helvetica Neue";
        line-height:1.7;
    }
    .loginTitle{
        margin: 0px auto 40px auto;
        text-align: center;
    }
    .loginHead{
        background: #409EFF;
    }
    .loginAside{
        width: 1000px;
        background: #4169E1;
    }
    .loginMain{
        background: #87CEFA;
        height:800px;
        flex-grow:1;
        background-image: url("../assets/bg.jpg");
        background-size:cover;
        background-repeat: no-repeat;
    }
    .loginFoot{
        background: #409EFF;
    }

</style>