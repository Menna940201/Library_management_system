
const signupForm = document.getElementById("signupForm");

if (signupForm) {
    signupForm.addEventListener("submit", function(event) {
        const password = document.getElementById("password")?.value;
        const confirmPassword = document.getElementById("confirm_password")?.value;
        const email = document.getElementById("email")?.value || "";
        const formMessage = document.getElementById("formMessage");

        if (formMessage) formMessage.textContent = "";

        if (password && confirmPassword && password !== confirmPassword) {
            event.preventDefault();
            if (formMessage) formMessage.textContent = "Passwords do not match.";
            return;
        }

        if (email && (!email.includes("@") || !email.includes("."))) {
            event.preventDefault();
            if (formMessage) formMessage.textContent = "Please enter a valid email.";
            return;
        }

        if (confirmPassword !== undefined && password !== confirmPassword) {
            event.preventDefault();
            if (formMessage) formMessage.textContent = "Passwords do not match.";
            return;
        }
    });
}


const searchInput = document.getElementById("searchInput");
const books = document.querySelectorAll(".book-card");
const searchType = document.getElementById("searchType");
const resultCount = document.getElementById("resultCount");
const noResults = document.getElementById("noResults");
const clearButton = document.getElementById("clearSearch");

if (searchInput) {
    searchInput.addEventListener("input", filterBooks);
}

if (searchType) {
    searchType.addEventListener("change", filterBooks);
}

if (clearButton) {
    clearButton.addEventListener("click", function() {
        searchInput.value = "";
        if (searchType) searchType.value = "all";
        filterBooks();
    });
}

function filterBooks() {
    const searchText = searchInput.value.toLowerCase().trim();
    let visibleBooks = 0;

    books.forEach(function(book) {
        const titleElement = book.querySelector(".book-title");
        const authorElement = book.querySelector(".book-author");
        const categoryElement = book.querySelector(".book-category");

        if (!titleElement || !authorElement) return;

        const title = titleElement.textContent.toLowerCase();
        const author = authorElement.textContent.toLowerCase();
        const category = categoryElement ? categoryElement.textContent.toLowerCase() : "";

        let selectedType = searchType ? searchType.value : "all";
        let match = false;

        if (selectedType === "title") {
            match = title.includes(searchText);
        } else if (selectedType === "author") {
            match = author.includes(searchText);
        } else if (selectedType === "category") {
            match = category.includes(searchText);
        } else {
            match = title.includes(searchText) || author.includes(searchText) || category.includes(searchText);
        }

        if (match) {
            book.style.display = "";
            visibleBooks++;
        } else {
            book.style.display = "none";
        }
    });

    if (resultCount) {
        resultCount.textContent = "Search Results: " + visibleBooks + " books";
    }

    if (noResults) {
        noResults.style.display = (visibleBooks === 0 && searchText !== "") ? "block" : "none";
    }
}


const protectedActions = document.querySelectorAll(".login-required");
const loginPopup = document.getElementById("loginPopup");
const closePopup = document.getElementById("closePopup");

if (protectedActions.length > 0 && loginPopup) {
    protectedActions.forEach(function(action) {
        action.addEventListener("click", function(event) {
            const userIsLoggedIn = (typeof window !== 'undefined' && window.isLoggedIn === true);

            if (!userIsLoggedIn && !action.querySelector('a')) {
                event.preventDefault();
                loginPopup.style.display = "flex";
            }
        });
    });
}

if (closePopup && loginPopup) {
    closePopup.addEventListener("click", function() {
        loginPopup.style.display = "none";
    });
}

document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".messages-container, #formMessage, div.alert, p[style*='color: #c0392b']");
    
    if (messages.length > 0) {
        setTimeout(function () {
            messages.forEach(function (msg) {
                msg.style.transition = "opacity 0.6s ease";
                msg.style.opacity = "0";
                
                setTimeout(function () {
                    msg.remove();
                }, 600);
            });
        }, 3000);
    }
});