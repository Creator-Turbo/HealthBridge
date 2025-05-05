$(document).ready(function(){
  $('.fa-bars').click(function(){
      $(this).toggleClass('fa-times');
      $('.navbar').toggleClass('nav-toggle');
  });
  $(Window).on('scroll load',function(){
      $('.fa-bars').removeClass('fa-times');
      $('.navbar').removeClass('nav-toggle');
      
      if($(Window).scrollTop()>30){
          $('header').addClass('header-active');
      }
      else{
          $('header').removeClass('header-active');
      }
  })
});


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
anchor.addEventListener("click", function (e) {
  e.preventDefault();
  const target = document.querySelector(this.getAttribute("href"));
  if (target) {
    target.scrollIntoView({
      behavior: "smooth"
    });
  }
});
});


function toggleChat() {
  const body = document.getElementById("chatbotBody");
  const toggleBtn = document.querySelector(".chat-toggle-btn");
  const isOpen = body.style.display === "block";

  if (isOpen) {
    body.style.display = "none";
    toggleBtn.style.display = "none";
  } else {
    body.style.display = "block";
    toggleBtn.style.display = "block";
  }
}


document.getElementById("appointmentBtn").onclick = function () {
  document.getElementById("formPopup").style.display = "block";
};

document.getElementById("closeForm").onclick = function () {
  document.getElementById("formPopup").style.display = "none";
};


document.querySelectorAll('.social-icons i').forEach(icon => {
  icon.addEventListener('click', () => {
    SubmitEvent(`${icon.classList[1].replace('fa-', '')}`);
  });
});




//document.querySelectorAll('.department').forEach(dep => {
  //dep.addEventListener('click', () => {
    //alert(`you clicked on ${dep.querySelector('p,a[herf^="#"').textContent}`);
    //SubmitEvent(`${dep.classList[1].replace('fa-', '')}`);
 // });
//});

function redirectTo(url) {
  window.location.href = url
}



// $(document).ready(function () {
//   $('.fa-bars').click(function () {
//     $(this).toggleClass('fa-times');
//     $('.navbar').toggleClass('nav-toggle');
//   });

//   $(window).on('scroll load', function () {
//     $('.fa-bars').removeClass('fa-times');
//     $('.navbar').removeClass('nav-toggle');

//     if ($(window).scrollTop() > 30) {
//       $('header').addClass('header-active');
//     } else {
//       $('header').removeClass('header-active');
//     }
//   });
// });

// document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//   anchor.addEventListener("click", function (e) {
//     e.preventDefault();
//     const target = document.querySelector(this.getAttribute("href"));
//     if (target) {
//       target.scrollIntoView({
//         behavior: "smooth"
//       });
//     }
//   });
// });

// function toggleChat() {
//   const body = document.getElementById("chatbotBody");
//   const toggleBtn = document.querySelector(".chat-toggle-btn");
//   const isOpen = body.style.display === "block";

//   if (isOpen) {
//     body.style.display = "none";
//     toggleBtn.style.display = "none";
//   } else {
//     body.style.display = "block";
//     toggleBtn.style.display = "block";
//   }
// }

// document.getElementById("appointmentBtn").onclick = function () {
//   document.getElementById("formPopup").style.display = "block";
// };

// document.getElementById("closeForm").onclick = function () {
//   document.getElementById("formPopup").style.display = "none";
// };

// document.querySelectorAll('.social-icons i').forEach(icon => {
//   icon.addEventListener('click', () => {
//     SubmitEvent(`${icon.classList[1].replace('fa-', '')}`);
//   });
// });

// // Uncomment this if needed
// // document.querySelectorAll('.department').forEach(dep => {
// //   dep.addEventListener('click', () => {
// //     alert(`you clicked on ${dep.querySelector('p,a[herf^="#"').textContent}`);
// //     SubmitEvent(`${dep.classList[1].replace('fa-', '')}`);
// //   });
// // });

// function redirectTo(url) {
//   window.location.href = url;
// }

// // ===========================
// // Login/Logout functionality
// // ===========================

// // Show login form
// document.getElementById("openLogin").onclick = function () {
//   document.getElementById("loginForm").style.display = "block";
//   this.style.display = "none";
// };

// // Login logic
// document.getElementById("loginBtn").onclick = function () {
//   const username = document.getElementById("usernameInput").value;
//   if (username) {
//     localStorage.setItem("loggedInUser", username);
//     updateUI();
//   }
// };

// // Logout logic
// document.getElementById("logoutBtn").onclick = function () {
//   localStorage.removeItem("loggedInUser");
//   updateUI();
// };

// // Function to update UI based on login status
// function updateUI() {
//   const user = localStorage.getItem("loggedInUser");
//   if (user) {
//     document.getElementById("userInfo").style.display = "block";
//     document.getElementById("loginForm").style.display = "none";
//     document.getElementById("openLogin").style.display = "none";
//     document.getElementById("welcomeText").textContent = `Welcome, ${user}`;
//   } else {
//     document.getElementById("userInfo").style.display = "none";
//     document.getElementById("loginForm").style.display = "none";
//     document.getElementById("openLogin").style.display = "inline-block";
//   }
// }

// // Run login UI logic on page load
// document.addEventListener("DOMContentLoaded", updateUI);
