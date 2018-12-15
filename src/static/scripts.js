function makePrediction(body) {
    const options =  {
        method: 'post',
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(body)
    }
    return fetch(`${window.location.origin}/api/v1/prediction`, options)
}

const submitButton = document.querySelector('button[type="submit"]');
const answerField = document.getElementById('answer');

function onSubmitClick(e) {
    e.preventDefault()
    disableButton(submitButton)
    answerField.innerHTML = 'Идёт подсчёт...';
    window.scrollTo({ top: document.body.offsetHeight,  behavior: 'smooth' });
    makePrediction(getInputValues())
    .then(response => response.text())
    .then(text => parseFloat(text))
    .then(float => float.toFixed(2))
    .then(text => answerField.innerHTML = `Рекомендуемая цена: $${text}`)
    .then(() => enableButton(submitButton))
}

function disableButton(button) {
    button.classList.add('disabled');
    button.setAttribute('disabled', true)
}

function enableButton(button) {
    button.classList.remove('disabled');
    button.removeAttribute('disabled');
}

const inputNameToValue = select => ({ [select.id]: select.value })
const toOneObject = (total, obj) => (Object.assign(total, obj))
const getInputValues = () => Array.from(document.querySelectorAll('select,input[type=text],input[type=number]')).map(inputNameToValue).reduce(toOneObject, {})