/*---------header---------*/
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');
let carouselDom = document.querySelector('.carousel');
let listItemDom = document.querySelector('.carousel .list');
let thumbnailDom = document.querySelector('.carousel .thumbnail');

nextDom.onclick = function(){
    showSlider('next');
}

prevDom.onclick = function(){
    showSlider('prev');
}
let timeRunning = 3000;
let timeAutoNext = 7000;
let runTimeOut;
let runAutoRun = setTimeout(() => {
    nextDom.click();
}, timeAutoNext);

function showSlider(type){
    let itemSlider = document.querySelectorAll('.carousel .list .item');
    let itemThumbnail = document.querySelectorAll('.carousel .thumbnail .item');

    if (type === 'next'){
        listItemDom.appendChild(itemSlider[0]);
        thumbnailDom.appendChild(itemThumbnail[0]);
        carouselDom.classList.add('next');
    }else{
        let positionLasItem = itemSlider.length - 1;
        listItemDom.prepend(itemSlider[positionLasItem]);
        thumbnailDom.prepend(itemThumbnail[positionLasItem]);
        carouselDom.classList.add('prev');
    }

    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() =>{
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning)

    clearTimeout(runAutoRun);
    runAutoRun = setTimeout(() => {
        nextDom.click();
    }, timeAutoNext);
}

/*---------main---------*/
let items = document.querySelectorAll('.conCon');
items.forEach(item => {
    item.addEventListener('mousemove', (e) => {
        // get position pointer in with (pixel)
        let positionPx = e.x -item.getBoundingClientRect().left;
        //convert to %
        let positionX = (positionPx / item.offsetWidth)*100;
        // get position pointer in height (px)
        let positionPy = e.y - item.getBoundingClientRect().top;
        // convert to %
        let positionY = (positionPy / item.offsetHeight)*100;

        item.style.setProperty('--rX', (0.5) * (50 - positionY) + 'deg');
        item.style.setProperty('--rY', -(0.5) * (50 - positionX) + 'deg');
    })
    item.addEventListener('mouseout', () => {
        item.style.setProperty('--rX', '0deg');
        item.style.setProperty('--rY', '0deg');
    })
})


// Middleware to check if user is logged in
function isAuthenticated(req, res, next) {
    if (req.isAuthenticated && req.isAuthenticated()) { // Assuming a function like `req.isAuthenticated()`
      return next();
    } else {
      res.redirect('/login');
    }
}
  
// Route to handle adding to cart
app.get('/add-to-cart', isAuthenticated, (req, res) => {
    // Logic for adding items to the cart
    res.send('Item added to cart');
});
  
// Route to handle viewing products
app.get('/products', isAuthenticated, (req, res) => {
    // Logic to show products
    res.send('Viewing products');
});
  
// Route to show the login page
app.get('/login', (req, res) => {
    res.send('Please log in to access this page.');
});
  
// Lấy các phần tử cần thiết
const userIcon = document.getElementById("userIcon");
const logoutMenu = document.getElementById("logoutMenu");

// Thêm sự kiện click vào icon người dùng để hiển thị menu logout
userIcon.addEventListener("click", function() {
  // Chuyển đổi giữa hiển thị và ẩn menu logout
  logoutMenu.style.display = logoutMenu.style.display === "block" ? "none" : "block";
});

// Nếu nhấn vào logout, bạn có thể thực hiện hành động logout (ví dụ: điều hướng đến trang đăng xuất)
document.getElementById("logoutBtn").addEventListener("click", function() {
  alert("Bạn đã đăng xuất.");
  // Chuyển hướng đến trang đăng xuất hoặc thực hiện hành động khác tại đây
  // window.location.href = '/logout'; 
});


