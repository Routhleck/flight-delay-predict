<template>
        <el-container>
  <el-aside width="200px" class="registerAside">
      <img src="../assets/th2.png" alt="" class="logo"/>
      <div class="gl">
      <el-dropdown>
               <span class="el-dropdown-link">
            前往登录<i class="el-icon-arrow-down el-icon--right"></i>
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
    <el-header class="registerHead">
        <i class="el-icon-help">航班延误预测系统</i>
    </el-header>
    <el-main class="registerMain">
        <el-form ref="registerform" :model="registerForm" status-icon :rules="rules" class="registerContainer">
            <h3 class="registerTitle">系统注册</h3>
            <el-form-item prop="username">
                <el-input type="text"
                          auto-complete="false"
                          v-model="registerForm.username"
                          placeholder="请输入用户名"
                          prefix-icon="el-icon-user-solid"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input type="password"
                          auto-complete="false"
                          v-model="registerForm.password"
                          placeholder="请输入密码"
                            prefix-icon="el-icon-key"></el-input>
            </el-form-item>
            <el-form-item prop="checked">
                <el-input type="password"
                          auto-complete="false"
                          v-model="registerForm.checked"
                          placeholder="请确认密码"
                          prefix-icon="el-icon-key"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" style="width:100%" @click="submitForm('registerForm')">注册</el-button>
              </el-form-item>
        </el-form>
    </el-main>
      <el-footer class="registerFoot">
          <div class="kaifa">国寄纵队小组开发出品</div>
      </el-footer>
  </el-container>
</el-container>

</template>

<script>
    export default {
        name: "Register",
        data(){
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    if (this.registerForm.checked !== '') {
                        this.$refs.registerForm.validateField('checkPass');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.registerForm.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
            return{
                registerForm:{
                    username:'',
                    password:'',
                },
                rules:{
                    username:[
                        {required: true, message: '请输入用户名', trigger: 'blur'},
                        { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
                    ],
                    password: [
                         { validator: validatePass, trigger: 'blur' }
                    ],
                    checked: [
                        { validator: validatePass2, trigger: 'blur' }
                    ]
                }
            }
        },
        methods: {
            toRegister() {
                this.$router.push({path: '/Register'})
            },
            toLogin() {
                this.$router.push({path: '/'})
            },
            submitForm(formName) {

                this.axios.post('http://localhost:5000/signup',this.registerForm).then((resp) =>{
                    let data = resp.data;
                    if(data.toString()=="true"){
                      this.registerForm = {};
                this.$message({
                    message: '注册成功',
                    type: 'success'
                });
                this.$router.push({path: '/'})
                    }
                })

            }
        }
    }
</script>

<style scoped>
    .registerContainer{
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
    .registerTitle{
        margin: 0px auto 40px auto;
        text-align: center;
    }
    .registerHead{
        background: #409EFF;
    }
    .registerAside{
        width: 1000px;
        background: #4169E1;
    }
    .registerMain{
        background: #87CEFA;
        height:800px;
        flex-grow:1;
        background-image: url("../assets/bg.jpg");
        background-size:cover;
        background-repeat: no-repeat;
    }
    .registerFoot{
        background: #409EFF;
    }

</style>