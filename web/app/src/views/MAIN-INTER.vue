<template>
        <el-container>
  <el-aside width="200px" class="mainAside">
      <img src="../assets/th2.png" alt="" class="logo"/>
      <div class="gl2">
          <el-dropdown>
               <span class="el-dropdown-link">
            用户管理<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
      <el-dropdown-menu slot="dropdown">
          <el-dropdown-item @click.native="checkadd()">用户列表</el-dropdown-item>
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
    <el-header class="mainHead">
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
    <el-main class="mainMain">
         <!--面包屑导航区域-->
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ path: '/MAIN-INTER' }" class="head-bread">首页</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="chartBox">
    <div id="mapChart" ></div>
       </div>
        <el-divider content-position="center" style="position: relative;"></el-divider>
        <div class="fenge">机场设置</div>
        <el-divider content-position="center" style="position: relative;"></el-divider>
        <el-container style="position: relative;">
        <el-aside>
            <div style="height: 20px"></div>
         <div class = "gl">
          <el-tag style="width: 110px; height: 50px">提示:</el-tag>
          <el-tag style="width: 110px; height: 50px" v-text="thehint"></el-tag>
      </div>
       <div class = "gl">
   <el-tag style="width: 110px; height: 50px">出发机场</el-tag>
           <el-tag class = "startAirport" style="width:110px; height: 50px" v-text="msg"></el-tag>
      </div>
      <div class = "gl">
   <el-tag style="width: 110px; height: 50px">目的机场</el-tag>
           <el-tag class = "endAirport" style="width: 110px; height: 50px" v-text="emsg"></el-tag>
      </div>
      <div class = "gl">
          <el-time-picker
                  v-model="mainForm.value1"
                  class="time_select"
                  placeholder="选择时间"
                  @change="timeSelected"
                  value-format="HH:mm" format="HH:mm">
          </el-time-picker>
      </div>
      <div class = "gl">
          <el-button round @click="buttonShow && sure()" style="position: relative">确定</el-button>
          <el-button round style="position: relative" @click.native="toCancel()">取消</el-button>
          </div>
        </el-aside>
        <el-main class="getmain">
            <el-table
                    :data="tableData"
                    style="width: 100%"
                    max-height="250">
                <el-table-column
                        fixed
                        prop="date"
                        label="出发机场编号"
                        width="250">
                </el-table-column>
                <el-table-column
                        prop="name"
                        label="出发机场"
                        width="250">
                </el-table-column>
                <el-table-column
                        prop="province"
                        label="目的机场编号"
                        width="250">
                </el-table-column>
                <el-table-column
                        prop="city"
                        label="目的机场"
                        width="250">
                </el-table-column>
                <el-table-column
                        prop="address"
                        label="出发时间"
                        width="250">
                </el-table-column>
            </el-table>
        </el-main>
        </el-container>
        <el-divider content-position="center" style="position: relative;"></el-divider>
        <div class="fenge">预测信息</div>
        <el-divider content-position="center" style="position: relative;"></el-divider>
      <div>
      <el-collapse v-model="activeNames" @change="handleChange" class = "ec">
          <el-collapse-item title="出发机场天气预测" name="1">
              <el-table :data="departureList" border stripe style="position:relative">
                  <el-table-column type="index"></el-table-column>
                  <el-tableColumn label="日期" prop="date"></el-tableColumn>
                  <el-tableColumn label="平均气温/°C" prop="avg_temp"></el-tableColumn>
                  <el-tableColumn label="最高气温/°C" prop="max_temp"></el-tableColumn>
                  <el-tableColumn label="最低气温/°C" prop="min_temp"></el-tableColumn>
                  <el-tableColumn label="降水量/mm" prop="prec"></el-tableColumn>
                  <el-tableColumn label="气压/kpa" prop="pressure"></el-tableColumn>
                  <el-tableColumn label="风向" prop="wind_dir"></el-tableColumn>
                  <el-tableColumn label="风速/ km/h" prop="wind_speed"></el-tableColumn>
              </el-table>
          </el-collapse-item>
          <el-collapse-item title="到达机场天气预测" name="2">
              <el-table :data="arriveList" border stripe style="position:relative">
                  <el-table-column type="index"></el-table-column>
                  <el-tableColumn label="日期" prop="date"></el-tableColumn>
                  <el-tableColumn label="平均气温/°C" prop="avg_temp"></el-tableColumn>
                  <el-tableColumn label="最高气温/°C" prop="max_temp"></el-tableColumn>
                  <el-tableColumn label="最低气温/°C" prop="min_temp"></el-tableColumn>
                  <el-tableColumn label="降水量/mm" prop="prec"></el-tableColumn>
                  <el-tableColumn label="气压/kpa" prop="pressure"></el-tableColumn>
                  <el-tableColumn label="风向" prop="wind_dir"></el-tableColumn>
                  <el-tableColumn label="风速/ km/h" prop="wind_speed"></el-tableColumn>
              </el-table>
          </el-collapse-item>
          <el-collapse-item title="延误预测" name="3">
              <el-table :data="totalList"  border stripe style="position:relative">
                  <el-table-column type="index"></el-table-column>
                  <el-tableColumn label="日期" prop="date"></el-tableColumn>
                  <el-tableColumn label="正常延误概率" prop="normal_prob"></el-tableColumn>
                  <el-tableColumn label="轻度延误概率" prop="mild_prob"></el-tableColumn>
                  <el-tableColumn label="中度延误概率" prop="moderate_prob"></el-tableColumn>
                  <el-tableColumn label="重度延误概率" prop="serious_prob"></el-tableColumn>
                  <el-tableColumn label="预测结果" prop="max_prob"></el-tableColumn>
              </el-table>
          </el-collapse-item>
      </el-collapse>
  </div>
    </el-main>
      <el-footer class="mainFoot">
          <div class="kaifa">国寄纵队小组开发出品</div>
      </el-footer>
  </el-container>
</el-container>
</template>

<script>
    import Vue from "vue";
    import echarts from "echarts";
    Vue.prototype.$echarts = echarts;
    import china from "echarts/map/json/china.json";
    echarts.registerMap("china", china);

    export default {
        name: "main",

        data() {
            return {
                mainForm: {
                     showmsg : '',
                     showemsg : '',
                     value1: '',
                },
                adminForm:{
                     username : this.$route.query.username,
                },
                buttonShow : false,
                count: 0,
                thehint : "请选择出发机场",
                msg : "请选择",
                emsg : "请选择",
                activeNames: ['0'],
                departureList : [],
                arriveList: [],
                totalList :[],

            }

        },

        mounted() {
            this.getMapChart();
          },
        methods: {
            openMsgHint(msg,data1) {
                this.$confirm('是否选择'+msg+'为出发机场', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$message({
                        type: 'success',
                        message: '选择成功!',
                    });
                    this.msg = msg;
                    this.mainForm.showmsg=this.getCode(data1,msg);
                    console.log(this.getCode(data1,msg));
                    this.thehint =  "请选择目的机场" ;
                    console.log('success');
                     this.axios.post('http://localhost:5000/setDepartureAirport',this.mainForm).then((resp)=>{
                     let data = resp.data;
                        let that = this;
                    let tempList = []
                    for(let i = 0;i<7;i++){
                         tempList.push({
                             date:resp.data.date[i].date,
                             avg_temp:resp.data.avg_temp[i].avg_temp,
                             max_temp:resp.data.max_temp[i].max_temp,
                             min_temp: resp.data.min_temp[i].min_temp,
                             prec: resp.data.prec[i].prec,
                             pressure: resp.data.pressure[i].pressure/10,
                             wind_dir: resp.data.wind_dir[i].wind_dir,
                             wind_speed: resp.data.wind_speed[i].wind_speed,
                         });
                    }
                    console.log(tempList);
                    that.departureList = tempList;

                })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消选择'
                    });
                });
            },
            openEMsgHint(msg,data1) {
                this.$confirm('是否选择'+msg+'为目的机场', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$message({
                        type: 'success',
                        message: '选择成功!',
                    });
                    this.emsg = msg;
                    this.mainForm.showemsg=this.getCode(data1,msg);
                    console.log(this.getCode(data1,msg));
                    this.thehint =  "请选择时间";
                    console.log('success');
                    this.axios.post('http://localhost:5000/setArriveAirport',this.mainForm).then((resp)=>{
                     let data = resp.data;
                        let that = this;
                    let tempList = []
                    for(let i = 0;i<7;i++){
                         tempList.push({
                             date:resp.data.date[i].date,
                             avg_temp:resp.data.avg_temp[i].avg_temp,
                             max_temp:resp.data.max_temp[i].max_temp,
                             min_temp: resp.data.min_temp[i].min_temp,
                             prec: resp.data.prec[i].prec,
                             pressure: resp.data.pressure[i].pressure/10,
                             wind_dir: resp.data.wind_dir[i].wind_dir,
                             wind_speed: resp.data.wind_speed[i].wind_speed,
                         });
                    }
                    console.log(tempList);
                    that.arriveList = tempList;

                })
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消选择'
                    });
                });
            },
            handleChange(val) {
                console.log(val);
            },
            timeSelected(){
                alert("change");
                if(this.msg!= "请选择" && this.emsg!="请选择"){
                    this.thehint = "请点击确认";
                    this.buttonShow = true;
                }
            },
            toCancel() {
                alert("取消");
                this.count= 0;
                this.thehint = "请选择出发机场";
                this.msg = "请选择",
                this.emsg = "请选择";
                return;
            },
            sure () {
                alert("确定");


                this.axios.post('http://localhost:5000/delayPredict',this.mainForm).then((resp)=>{
                     let data = resp.data;
                        let that = this;

                     //that.mildList = resp.data.mild_prob;
                    let tempList = []
                    for(let i = 0;i<7;i++){
                         tempList.push({
                             date:resp.data.date[i].date,
                             normal_prob:resp.data.normal_prob[i].normal_prob,
                             mild_prob:resp.data.mild_prob[i].mild_prob,
                             moderate_prob: resp.data.moderate_prob[i].moderate_prob,
                             serious_prob: resp.data.serious_prob[i].serious_prob,
                             max_prob: resp.data.max_prob[i].max_prob
                         });
                    }
                    console.log(tempList);
                    that.totalList = tempList;
                     //console.log(resp.data.normal_prob);
                    // // for( let i =0; i<15; i++){
                    // //     console.log(data1[0][i].toString());
                    // // }
                    // if(data.toString()!= null){
                    //     this.axios.post('http://localhost:5000/setArriveAirport',this.mainForm).then((resp)=>{
                    //         let data = resp.data;
                    //         if(data.toString()=="true"){
                    //             this.axios.post('http://localhost:5000/delayPredict',this.mainForm).then((resp)=>{
                    //                 let data = resp.data;
                    //                 console.log(data);
                    //             })
                    //         }
                    //         this.$message({
                    //             message: '选择成功',
                    //             type: 'success'
                    //         });
                    //     })
                    // }
                })
             },
            checkadd(){
                this.axios.post('http://localhost:5000/judgeAdmin',this.adminForm).then((resp)=>{
                    let data = resp.data;
                    if(data.toString()=="true"){
                     this.$router.push({path:'/Manager'})
                    }else {
                        this.$message({
                                message: '你没有权限',
                                type:'error'
                            });
                    }
                })
            },
            exits(){
                this.$router.push({path: '/'})
            },
            getMapChart() {
                  var hintGroup = this.getHint();
                  var dataValue = this.dealWithData();
                  var data1 = dataValue.splice(0, 27);
                  var myChart = this.$echarts.init(document.getElementById("mapChart"))
                  var option = {
                    tooltip: {
                      show: false,
                    },
                    backgroundColor: "rgba(0,0,0,0)",
                    geo: {
                      map: "china",
                      roam: false, // 一定要关闭拖拽
                      zoom: 1.23,
                      center: [105, 36], // 调整地图位置
                      label: {
                        normal: {
                          show: false, //关闭省份名展示
                          fontSize: "10",
                          color: "rgba(0,0,0,0.7)",
                        },
                        emphasis: {
                          show: false,
                        },
                      },
                      itemStyle: {
                        normal: {
                          areaColor: "#0d0059",
                          borderColor: "#389dff",
                          borderWidth: 1, //设置外层边框
                          shadowBlur: 5,
                          shadowOffsetY: 8,
                          shadowOffsetX: 0,
                          shadowColor: "#01012a",
                        },
                        emphasis: {
                          areaColor: "#184cff",
                          shadowOffsetX: 0,
                          shadowOffsetY: 0,
                          shadowBlur: 5,
                          borderWidth: 0,
                          shadowColor: "rgba(0, 0, 0, 0.5)",
                        },
                      },
                    },
                    legend: {
                      orient: "horizontal",
                      height: "50%",
                      top: "0%",
                      right: "10%",
                    },
                    series: [
                      {
                        type: "map",
                        map: "china",
                        roam: false,
                        zoom: 1.23,
                        center: [105, 36],
                        // geoIndex: 1,
                        // aspectScale: 0.75, //长宽比
                        showLegendSymbol: false, // 存在legend时显示
                        label: {
                          // 显示地图省名称
                          normal: {
                            color: "#389dff",
                            formatter: "{b}",
                            position: [-12, -1],
                            show: false,
                          },
                          emphasis: {
                            show: false,
                          },
                        },
                        itemStyle: {
                          normal: {
                            areaColor: "#0d0059",
                            borderColor: "#389dff",
                            borderWidth: 0.5,
                          },
                          emphasis: {
                            areaColor: "#17008d",
                            shadowOffsetX: 0,
                            shadowOffsetY: 0,
                            shadowBlur: 5,
                            borderWidth: 0,
                            shadowColor: "rgba(0, 0, 0, 0.5)",
                          },
                        },
                      },
                      {
                        name: "",
                        type: "scatter",
                        coordinateSystem: "geo",
                        data: dataValue,
                        symbol: "circle",
                        symbolSize: 5,
                        hoverSymbolSize: 10,
                        tooltip: {
                          formatter(value) {
                            return (
                              value.data.name + "<br/>"
                            );
                          },
                          show: true,
                        },
                        encode: {
                          value: 2,
                        },
                        label: {
                          formatter: "{b}",
                          position: "right",
                          show: false,
                        },
                        itemStyle: {
                          color: "#0efacc",
                        },
                        emphasis: {
                          label: {
                            show: false,
                          },
                        },
                      },
                      {
                        name: "显示所有机场",
                        type: "effectScatter",
                        coordinateSystem: "geo",
                        data: data1,
                          textColor:"#000",
                        symbolSize: 8,

                        tooltip: {
                          formatter(value) {
                            return (
                              value.data.name + "<br/>"
                                // + "门店数：" + value.data.value[2]
                            );
                          },
                          show: true,
                        },
                        encode: {
                          value: 2,
                        },
                        showEffectOn: "render",
                        rippleEffect: {
                          brushType: "stroke",
                          color: "#0efacc",
                          period: 9,
                          scale: 5,
                        },
                        hoverAnimation: true,
                        label: {
                          formatter: "{b}",
                          position: "right",
                          show: true,
                        },
                        itemStyle: {
                          color: "#0efacc",
                          shadowBlur: 2,
                          shadowColor: "#333",
                        },
                        zlevel: 1,
                      },
                    ],
                  };
                  myChart.setOption(option);
                  myChart.on("click", (params) => {
                    console.log(params.seriesType);
                    if(params.seriesType == "effectScatter"){

                        if(this.thehint == "请选择出发机场"){
                        this.openMsgHint(params.name,data1)
                        }
                        else if(this.thehint == "请选择目的机场"){
                        this.openEMsgHint(params.name,data1)
                        }
                        else if(this.thehint == "请点击确认"){
                            alert("请点击确定或取消");
                            this.buttonShow = false;
                        }
                    }

                    return;
                    this.$router.push({
                      path: "/mapEchartProvince",
                      query: { provinceName: params.data.ename, province: params.name },
                    });
                  });
                  myChart.setOption(option);
                  window.onresize = () => {
                    myChart.resize();
                  };
                },
                 getHint() {
                   var hintsGroup = ["请选择出发机场", "请选择目的机场", "请点击确定" ];
                   return hintsGroup;
                 },
                dealWithData() {
                  var geoCoordMap = [
                    {
                      name: "罗家机场",
                      value: [117.18, 29.27, "JDZ"],
                    },
                    {
                      name: "浦东机场",
                      value: [121.80, 31.16, "PVG"],
                    },
                    {
                      name: "通辽机场",
                      value: [122.256, 43.62, "TGO"],
                    },
                    {
                      name: "高崎国际机场",
                      value: [118.03, 24.48, "XMN"],
                    },
                    {
                      name: "地窝堡国际机场",
                      value: [88.31, 43.36, "URC"],
                    },
                    {
                      name: "武宿国际机场",
                      value: [112.487, 37.94, "TYN"],
                    },
                    {
                      name: "宝安机场",
                      value: [113.88, 22.55, "SZX"],
                    },
                    {
                      name: "凤凰国际机场",
                      value: [109.75, 18.4, "SYX"],
                    },
                    {
                      name: "流亭国际机场",
                      value: [120.396, 36.9, "TAO"],
                    },
                    {
                      name: "遥墙国际机场",
                      value: [116.75, 35.8, "TNA"],
                    },
                    {
                      name: "正定机场",
                      value: [115.0, 40.03,"SJW"],
                    },
                    {
                      name: "桃仙国际机场",
                      value: [123.47, 41.8,"SHE"],
                    },
                    {
                      name: "虹桥机场",
                      value: [122.34, 30.196,"SHA"],
                    },
                    {
                      name: "首都国际机场",
                      value: [116.35, 39.04,"PEK"],
                    },
                    {
                      name: "禄口国际机场",
                      value: [119.89, 32.33,"NKG"],
                    },
                    {
                      name: "两江国际机场",
                      value: [110.3, 25.3,"KWL"],
                    },
                    {
                      name: "长水国际机场",
                      value: [101.82, 24.9, "KMG"],
                    },
                    {
                      name: "太平机场",
                      value: [126.96, 45.55, "HRB"],
                    },
                    {
                      name: "白塔机场",
                      value: [111.62, 40.8,"HET"],
                    },
                    {
                      name: "萧山国际机场",
                      value: [120.21, 28.2,"HGH"],
                    },
                    {
                      name: "长乐国际机场",
                      value: [119.27, 26.04,"FOC"],
                    },
                    {
                      name: "双流机场",
                      value: [104.1, 30.66,"CTU"],
                    },
                    {
                      name: "江北机场",
                      value: [106.54, 29.4,"CKG"],
                    },
                    {
                      name: "合肥机场",
                      value: [117.3, 31.69,"HFE"],
                    },
                    {
                      name: "新郑国际机场",
                      value: [113.64, 34.72,"CGO"],
                    },
                    {
                      name: "吐鲁番交河机场",
                      value: [89.2, 40.94,"TLQ"],
                    },
                    {
                      name: "天河机场",
                      value: [114.03, 30.58,"WUH"],
                    },
                  ];
                  return geoCoordMap;
                },
                 getCode(data2,name1){
                 for(let i = 0;i < data2.length;i++){
                     if(data2[i].name == name1){
                         return data2[i].value[2];
                     }
                 }
                 return "out";
                 },
              },

    }
</script>

<style scoped>
    .fenge{
        text-align: center;
        font-size: 40px;
        background: #409EFF;
        color: #fff;
    }
    .getmain{
        height: 300px;
    }

    .chartBox {
  width: 100%;
  height: 100vh;
}

    #mapChart {
      width: 100%;
      height: 100%;
    }
     .head-bread{
        position: relative;
         color: #fff;
         font-size: 20px;
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
    .mainHead{
        background: #409EFF;
        display: flex;
        justify-content: space-between;
    }
    .mainAside{
        width: 1000px;
        background: #4169E1;
    }
    .mainMain{
        background: #87CEFA;
        height:800px;
        flex-grow:1;
        background-image: url("../assets/bg.jpg");
        background-size:cover;
        background-repeat: no-repeat;
    }
    .mainFoot{
        background: #409EFF;
    }
    .ec{
        position: relative;
    }
    .time_select{
        max-width:100%;
        height:auto;

    }

</style>