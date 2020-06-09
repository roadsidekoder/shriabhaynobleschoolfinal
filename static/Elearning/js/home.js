document.getElementById('menuBtn').addEventListener('click', function(){
  document.getElementById('app').classList.add('opened'); 
});

document.getElementById('sideNavBg').addEventListener('click', function(){
  document.getElementById('app').classList.remove('opened'); 
});

document.getElementById('sideNavBg').addEventListener('click', function(){
  document.getElementById('app').classList.remove('opened'); 
});

 /* document.querySelectorAll('.accordion-header').forEach(accordionHeader => {
  accordionHeader.addEventListener('click', () => {
    const accordionContent = accordionHeader.nextElementSibling;
    accordionHeader.classList.toggle('active');    
    accordionContent.classList.toggle('active');
    
    if(accordionContent.classList.contains('active')) {
      accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
    } else {
      accordionContent.style.maxHeight = 0;
    }
  })
})
*/

const accordions = document.querySelectorAll('.accordion-header');

const closeOtherOpenAccordions = (target) => {
  accordions.forEach((accordion) => {
    if (accordion.classList.contains('active') && target !== accordion) {
      accordion.classList.remove('active');
      accordion.nextElementSibling.classList.remove('active')
      accordion.nextElementSibling.style.maxHeight = 0
    }
  })
}

accordions.forEach(accordion => {
  accordion.addEventListener('click', (e) => {
    const accordionContent = accordion.nextElementSibling;

    accordion.classList.toggle('active');

    accordionContent.classList.toggle('active');

    if (accordionContent.classList.contains('active')) {
      accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
    } else {
      accordionContent.style.maxHeight = 0;
    }
    closeOtherOpenAccordions(e.target)
  })
})