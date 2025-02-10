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


// Get the toggle button
const themeToggle = document.getElementById('theme-toggle');

// Check the user's preference and set the initial theme
const userPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark' || (!savedTheme && userPrefersDark)) {
  document.documentElement.classList.add('dark');
} else {
  document.documentElement.classList.remove('dark');
}

// Toggle dark mode and save the preference
themeToggle.addEventListener('click', () => {
  if (document.documentElement.classList.contains('dark')) {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  } else {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  }
});
