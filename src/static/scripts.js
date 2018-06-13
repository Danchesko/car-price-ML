function makePrediction(body) {
    const options =  {
        method: 'post',
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify(body)
    }
    return fetch(`${window.location.origin}/api/prediction`, options)
}

function onSubmitClick(e) {
    e.preventDefault()
    makePrediction(getInputValues())
    .then(response => response.text())
    .then(text => parseFloat(text))
    .then(float => float.toFixed(2))
    .then(text => document.getElementById('answer').innerHTML = `Рекомендуемая цена: $${text}`)
    .then(() => window.scrollTo(0,document.body.scrollHeight));
}

const inputNameToValue = select => ({ [select.id]: select.value })
const toOneObject = (total, obj) => (Object.assign(total, obj))
const getInputValues = () => Array.from(document.querySelectorAll('select,input[type=text],input[type=number]')).map(inputNameToValue).reduce(toOneObject, {})


