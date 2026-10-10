import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Scientific Calculator V2", page_icon="✨", layout="centered")
st.markdown("<style>#MainMenu, footer, header {visibility:hidden;} .stApp{background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);}</style>", unsafe_allow_html=True)

calc_v2 = """
<div id="wrap">
<style>
  *{margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', sans-serif;}
  #wrap{display:flex; justify-content:center; padding:10px;}
  .calc{
    width:390px; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px);
    border-radius:32px; padding:24px; box-shadow: 0 30px 80px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.2);
  }
  .display{
    background: linear-gradient(145deg, #0f172a, #1e293b); 
    border-radius:20px; padding:22px; min-height:120px; text-align:right; 
    margin-bottom:20px; box-shadow: inset 0 2px 10px rgba(0,0,0,0.5);
    border: 1px solid #334155;
  }
  .expr{color:#5eead4; font-size:20px; min-height:24px; word-break:break-all; font-family: monospace; opacity:0.9;}
  .res{color:#f8fafc; font-size:44px; font-weight:900; min-height:50px; word-break:break-all; margin-top:8px; text-shadow: 0 0 15px rgba(94,234,212,0.4);}
  .top-row{display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;}
  .badge{background:#0f172a; color:#22d3ee; border:1px solid #164e63; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:800; letter-spacing:1px;}
  
  .grid{display:grid; grid-template-columns:repeat(4, 1fr); gap:12px;}
  button{
    height:62px; border:none; border-radius:16px; font-size:18px; font-weight:800;
    cursor:pointer; transition: all 0.15s; outline:none;
  }
  button:active{transform:scale(0.90);}

  /* CHANGED COLORS */
  .num{background:#ffffff; color:#0f172a; box-shadow: 0 4px 0 #e2e8f0; border: 1px solid #f1f5f9;} 
  .num:hover{transform: translateY(-2px); box-shadow: 0 6px 0 #e2e8f0;}
  .op{background: linear-gradient(135deg, #f43f5e, #ec4899); color:white; box-shadow: 0 4px 0 #be123c;} 
  .sci{background: linear-gradient(135deg, #0f172a, #334155); color:#5eead4; font-size:14px; box-shadow: 0 4px 0 #020617; border: 1px solid #334155;}
  .eq{background: linear-gradient(135deg, #06ffa5, #00d2ff); color:#0f172a; grid-column: span 2; font-size:28px; box-shadow: 0 4px 0 #0891b2;}
  .ac{background: linear-gradient(135deg, #f97316, #fb923c); color:white; box-shadow: 0 4px 0 #9a3412;}
  .wide{grid-column: span 2;}
</style>

<div class="calc">
  <div class="display">
    <div class="expr" id="expr"></div>
    <div class="res" id="res">0</div>
  </div>
  
  <div class="top-row">
    <div class="badge" id="mode">DEG • ⌨️ ACTIVE</div>
    <div class="badge" style="color:#fb7185;">SCIENTIFIC V2</div>
  </div>

  <div class="grid">
    <button class="sci" onclick="add('sin(')">sin</button>
    <button class="sci" onclick="add('cos(')">cos</button>
    <button class="sci" onclick="add('tan(')">tan</button>
    <button class="ac" onclick="clearAll()">AC</button>

    <button class="sci" onclick="add('sqrt(')">√</button>
    <button class="sci" onclick="add('log(')">log</button>
    <button class="sci" onclick="add('ln(')">ln</button>
    <button class="ac" style="background:linear-gradient(135deg,#6366f1,#8b5cf6); box-shadow:0 4px 0 #4338ca;" onclick="del()">DEL</button>

    <button class="sci" onclick="add('π')">π</button>
    <button class="sci" onclick="add('e')">e</button>
    <button class="sci" onclick="add('^')">xʸ</button>
    <button class="sci" onclick="add('!')">n!</button>

    <button class="num" onclick="add('7')">7</button>
    <button class="num" onclick="add('8')">8</button>
    <button class="num" onclick="add('9')">9</button>
    <button class="op" onclick="add('/')">÷</button>

    <button class="num" onclick="add('4')">4</button>
    <button class="num" onclick="add('5')">5</button>
    <button class="num" onclick="add('6')">6</button>
    <button class="op" onclick="add('*')">×</button>

    <button class="num" onclick="add('1')">1</button>
    <button class="num" onclick="add('2')">2</button>
    <button class="num" onclick="add('3')">3</button>
    <button class="op" onclick="add('-')">−</button>

    <button class="num" onclick="add('0')">0</button>
    <button class="num" onclick="add('.')">.</button>
    <button class="op" onclick="add('+')">+</button>
    <button class="sci" onclick="toggleMode()" style="font-size:11px;">DEG/RAD</button>

    <button class="num" onclick="add('(')">(</button>
    <button class="num" onclick="add(')')">)</button>
    <button class="eq" onclick="calc()">=</button>
  </div>
</div>

<script>
let expr=""; let isDeg=true;
const exprEl=document.getElementById('expr'); const resEl=document.getElementById('res'); const modeEl=document.getElementById('mode');
function update(){ exprEl.innerText=expr||""; if(expr==="") resEl.innerText="0"; }
function add(v){ 
  if(v==='π') expr+='Math.PI'; else if(v==='e') expr+='Math.E'; else expr+=v; update(); 
}
function clearAll(){ expr=""; resEl.innerText="0"; update(); }
function del(){ expr=expr.slice(0,-1); update(); }
function toggleMode(){ isDeg=!isDeg; modeEl.innerText=(isDeg?"DEG":"RAD")+" • ⌨️ ACTIVE"; }
function factorial(n){ let r=1; for(let i=2;i<=n;i++) r*=i; return r; }
function calc(){
  try{
    let e=expr.replace(/\\^/g,'**');
    e=e.replace(/sqrt\\(/g,'Math.sqrt(').replace(/log\\(/g,'Math.log10(').replace(/ln\\(/g,'Math.log(');
    e=e.replace(/sin\\(/g, isDeg?'(Math.sin(Math.PI/180*':'(Math.sin(');
    e=e.replace(/cos\\(/g, isDeg?'(Math.cos(Math.PI/180*':'(Math.cos(');
    e=e.replace(/tan\\(/g, isDeg?'(Math.tan(Math.PI/180*':'(Math.tan(');
    e=e.replace(/(\\d+)!/g,'factorial($1)').replace(/factorial\\(/g,'factorial(');
    let r=eval(e); r=parseFloat(r.toFixed(10)); resEl.innerText=r; expr=String(r); exprEl.innerText="";
  }catch{ resEl.innerText="Error"; }
}
document.addEventListener('keydown', (ev)=>{
  const k=ev.key;
  if((k>='0' && k<='9') || ['+','-','*','/','(',')','.','%','^'].includes(k)){ add(k); ev.preventDefault(); }
  else if(k==='Enter' || k==='='){ calc(); ev.preventDefault(); }
  else if(k==='Backspace'){ del(); ev.preventDefault(); }
  else if(k==='Escape'){ clearAll(); }
});
update();
</script>
</div>
"""

components.html(calc_v2, height=820)

