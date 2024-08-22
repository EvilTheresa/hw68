
async function makeRequest(url, method = "GET", data=undefined) {
    let csrfToken = await getCookie('csrftoken')
    let headers = {
        'Content-Type': 'application/json',
    };
    if (method !== "GET") {
        headers['X-CSRFToken'] = csrfToken
    }
    let response = await fetch(url,
        {
            method: method,
            headers: headers,
            body: JSON.stringify(data)
        }
    );
    if (response.ok) {
        return await response.json();
    } else {
        let errorText = await response.text();
        let error = new Error(`HTTP Error: ${response.status}: ${errorText}`);
        console.log(error);
        throw error;
    }
}

async function numOper(operation) {
    let inputA = document.getElementById('inputA').value;
    let inputB = document.getElementById('inputB').value;
    let data = { A: parseInt(inputA, 10), B: parseInt(inputB, 10) };

    let url = `/api/v1/${operation}/`;

    try {
        let response = await makeRequest(url, "POST", data);
        document.getElementById('result').innerText = `Result: ${response.answer}`;
        document.getElementById('result').style.color = 'green';
    } catch (error) {
        document.getElementById('result').innerText = `Error: ${error.message}`;
        document.getElementById('result').style.color = 'red';
    }
}

function onLoad() {
    let buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener("click", () => numOper(button.getAttribute('data-operation')));
    });
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
window.addEventListener("load", onLoad);