//creating promises a corriger
const promise=newPromise((resolve,reject)=>{
    setTimeout(() => {
        resolve("data back from the server");
        
    } 3000);
    setTimeout() =>{
        rejectect("no data back from the server, there was en error")
    } 2000;
        
    };

    promise.then(response =>{
        console.log(response);
    }).catch(error =>{
        console.log(error);
    
})