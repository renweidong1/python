/**
 * Created by tarena on 18-10-12.
 */
var n = 0;
var timer = null;
var ctx;
var input_time;
function init(){
    var can = document.getElementById("can");
    ctx = can.getContext('2d');
    ctx.strokeStyle = "#000";
    input_time = document.getElementsByTagName("input")[0];
    for(var i=0;i<14;i++){
        for(var j=0;j<14;j++){
            ctx.strokeRect(j*40+60,i*40+60,40,40)
        }
    }
}
function begin_time() {
    clearInterval(timer);
    timer=setInterval(function () {
        n++;
        var m=parseInt(n/3600);
        var s=parseInt(n/60%60);
        var M=parseInt(n%60);
        input_time.value=toDub(m)+":"+toDub(s)+":"+toDub(M);
    },1000/60)
}
function toDub(n){
    return n<10?"0"+n:""+n;
}
var url ='../static/music/water.wav';
var con = new AudioContext();
function voice(url_data){
    var req = new XMLHttpRequest();
    req.open("GET",url_data,true);
    req.responseType = 'arraybuffer';
    req.onload = function () {
        con.decodeAudioData(req.response,function (buffer){
            //播放声音
            var source = con.createBufferSource();
            source.buffer = buffer;
            source.connect(con.destination);
            source.start(0);
        },function (e) {
            console.info('错误');
        });
    };
    req.send(null);
}
