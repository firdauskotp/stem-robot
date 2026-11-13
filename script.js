(() => {
 const toggle=document.querySelector('.nav-toggle');const nav=document.querySelector('#site-nav');
 toggle?.addEventListener('click',()=>{const open=nav.classList.toggle('is-open');toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
 nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('is-open');toggle?.setAttribute('aria-expanded','false');toggle?.setAttribute('aria-label','Open navigation');}));
 const samples={
  paper:{name:'Rubbish',desc:'A paper ball could be classified as rubbish. We would still check whether the prediction is correct.',icon:'▤',colour:'#79526d'},
  pencil:{name:'Not rubbish',desc:'A pencil is a useful classroom item. The robot should ignore it instead of treating every object as rubbish.',icon:'✎',colour:'#3e6a73'},
  empty:{name:'Empty',desc:'When there is nothing in the camera’s test area, the correct category is empty.',icon:'○',colour:'#77716f'}
 };
 document.querySelectorAll('[data-case]').forEach(btn=>btn.addEventListener('click',()=>{
  const ex=samples[btn.dataset.case];if(!ex)return;
  document.querySelectorAll('[data-case]').forEach(x=>{x.classList.toggle('selected',x===btn);x.setAttribute('aria-pressed',String(x===btn));});
  document.querySelector('#example-label').textContent=ex.name;
  document.querySelector('#example-description').textContent=ex.desc;
  const icon=document.querySelector('#example-icon');icon.textContent=ex.icon;icon.style.background=ex.colour;
 }));
})();
