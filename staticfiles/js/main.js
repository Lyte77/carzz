document.getElementById('menu-toggle').addEventListener(
    'click', () =>{
        const mobileMenu = document.getElementById('mobile-menu');
        mobileMenu.classList.toggle('hidden');
    }
)

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.accordion').forEach(elm => {
      const button = elm.querySelector('.toggle-button');
      const content = elm.querySelector('.content');
      const plusIcon = button.querySelector('.plus');

      button.addEventListener('click', () => {
        const isHidden = content.classList.toggle('invisible');
        content.style.maxHeight = isHidden ? '0px' : `${content.scrollHeight + 100}px`;
        button.classList.toggle('text-blue-600', !isHidden);
        button.classList.toggle('text-gray-800', isHidden);
        content.classList.toggle('pb-6', !isHidden);
        plusIcon.classList.toggle('hidden', !isHidden);
        plusIcon.classList.toggle('block', isHidden);
      });
    });
  });

// Carousel section
let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-slide');
const dots = document.querySelectorAll('.carousel-dot');

// Initialize carousel
function initCarousel() {
    showSlide(0);
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
        });
    });
    document.getElementById('prevBtn').addEventListener('click', prevSlide);
    document.getElementById('nextBtn').addEventListener('click', nextSlide);
    setInterval(nextSlide, 5000);
}

// Show the specified slide
function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.classList.toggle('opacity-100', i === index);
        slide.classList.toggle('opacity-0', i !== index);
    });
    dots.forEach((dot, i) => {
        dot.classList.toggle('bg-white', i === index);
        dot.classList.toggle('bg-white/50', i !== index);
    });
    currentSlide = index;
}

// Navigate to the next slide
function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

// Navigate to the previous slide
function prevSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
}

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', initCarousel);

// Initialization for ES Users
import {
  Carousel,
  initTWE,
} from "tw-elements";

initTWE({ Carousel });