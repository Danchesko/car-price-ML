function makePrediction(body) {
    const options =  {
        method: 'post',
        headers: {
          "Content-type": "application/json"
        },
        body
    }
    return fetch('localhost:5000/api/prediction', options)
}

function onSubmitClick(e) {
    e.preventDefault()
    makePrediction(getInputValues())    
}

const inputNameToValue = select => ({ [select.id]: select.value })
const toOneObject = (total, obj) => (Object.assign(total, obj))
const getInputValues = () => Array.from(document.querySelectorAll('select,input[type=text],input[type=number]')).map(inputNameToValue).reduce(toOneObject, {})



