const ctx = document.getElementById('weeklyChart').getContext('2d');
new Chart(ctx,{
    type:'line',
    data:{
        labels:['Lun','Mar','Mié','Jue','Vie','Sáb','Dom'],
        datasets:[{
            label:'Accesos',
            data: window.accesses_week || [0,0,0,0,0,0,0],
            backgroundColor:'rgba(0,255,255,0.3)',
            borderColor:'#0ff',
            borderWidth:3,
            tension:0.4,
            fill:true,
            pointBackgroundColor:'#0ff',
            pointRadius:6,
            pointHoverRadius:10
        }]
    },
    options:{ responsive:true, animation:{duration:2000, easing:'easeOutQuart'} }
});
// Partículas flotantes
const particlesDiv = document.getElementById('particles');
const canvas = document.createElement('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
particlesDiv.appendChild(canvas);
const ctxParticles = canvas.getContext('2d');
const particles = [];
for(let i=0;i<80;i++){
  particles.push({
    x: Math.random()*canvas.width,
    y: Math.random()*canvas.height,
    r: Math.random()*3+1,
    dx: (Math.random()-0.5)*1.5,
    dy: (Math.random()-0.5)*1.5,
    alpha: Math.random()
  });
}
function animateParticles(){
  ctxParticles.clearRect(0,0,canvas.width,canvas.height);
  for(let p of particles){
    ctxParticles.beginPath();
    ctxParticles.arc(p.x,p.y,p.r,0,Math.PI*2);
    ctxParticles.fillStyle=`rgba(0,255,255,${p.alpha})`;
    ctxParticles.fill();
    p.x+=p.dx; p.y+=p.dy;
    if(p.x<0||p.x>canvas.width)p.dx*=-1;
    if(p.y<0||p.y>canvas.height)p.dy*=-1;
  }
  requestAnimationFrame(animateParticles);
}
animateParticles();
window.addEventListener('resize',()=>{canvas.width=window.innerWidth; canvas.height=window.innerHeight;});