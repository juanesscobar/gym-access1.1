const ctx=document.getElementById('weeklyChart').getContext('2d');
new Chart(ctx,{
  type:'line',
  data:{
    labels:['Lun','Mar','Mié','Jue','Vie','Sáb','Dom'],
    datasets:[{
      label:'Accesos',
      data:[50,75,60,90,120,110,95],
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
  options:{
    responsive:true,
    animation:{ duration:2000, easing:'easeOutQuart' },
    plugins:{ legend:{ display:false } },
    scales:{
      y:{ beginAtZero:true, grid:{ color:'rgba(0,255,255,0.1)' }, ticks:{ color:'#0ff', font:{ weight:600 } } },
      x:{ grid:{ color:'rgba(0,255,255,0.1)' }, ticks:{ color:'#0ff', font:{ weight:600 } } }
    }
  }
});
