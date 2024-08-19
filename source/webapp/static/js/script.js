async function makeRequest(url, method = 'POST') {
    const csrfToken = document.body.getAttribute('data-csrf-token');
    let response = await fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
    });
    if (response.ok) {
        return await response.json();
    } else {
        let errorText = await response.text();
        let error = new Error(`HTTP Error: ${response.status}: ${errorText}`);
        console.error(error);
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let button = event.target;
    let articleId = button.getAttribute('data-article-id');


    let url = `/api/article/${articleId}/toggle_like/`;
    try {
        let response = await makeRequest(url);
        console.log(response);
        button.innerText = response.liked ? 'Unlike' : 'Like';
        let likesCounter = document.querySelector('.likes-count');
        likesCounter.innerText = `Likes: ${response.likes_count}`;
    } catch (error) {
        console.error('Error toggling like:', error);
    }
}


function onLoad() {
    let buttons = document.querySelectorAll('[data-js="like-button"]');
    for (let button of buttons) {
        button.addEventListener("click", onClick);
    }
}

document.addEventListener('DOMContentLoaded', onLoad);
