const DECISION_THRESHOULD = 75
let isAnimating = false
let pullDeltaX = 0 // distance que la card se está arrastrando 

function startDrag (event) {
    if (isAnimating) return

    //get the first article element
    const actualCard = event.target.closest('article')

    //get initial position of mouse of finger
    const startX = event.pageX ?? event.touches[0].pageX


    //listen the mouse and touch movemente
    document.addEventListener('mousemove', onMove)
    document.addEventListener('mouseup', onEnd) 

    document.addEventListener('touchmove', onMove, { passive:true})
    document.addEventListener('touchend', onEnd, { passive:true}) 

    function onMove (event) {
        //current position of mouse or finger 
        const currentX = event.pageX ?? event.touches[0].page.x
        //the distance between the initial and current position 
        pullDeltaX = currentX - startX
        // no hay distancia recorrida 
        if (pullDeltaX === 0) return
        // change the flag to indicate we are animating 
        isAnimating = true 
        // calculate the rotation of the card using the distance 
        const deg = pullDeltaX / 10 
        //apply the transformation to the card
        actualCard.style.transform = `translateX(${pullDeltaX}px) rotate(${deg}deg)`
        // change the cursor to grabbing 
        actualCard.style.cursor = 'grabbbing'
       
    }
    
    function onEnd (event) {
        document.removeEventListener('mousemove', onMove)
        document.removeEventListener('mouseup', onEnd)
    

        document.removeEventListener('touchmove', onMove)
        document.removeEventListener('touchend', onEnd)


        //TODO: TO REMOVE AS WE'RE  DOING THIS OTHER WAY 
        //reset the flag 
        isAnimating = false 
        //reset the distance 
        pullDeltaX = 0 
        // reset the transformation 
        actualCard.style.transform = 'none'
        // reset the cursor 
        actualCard.style.cursor = 'grab'


        // saber su el usuario tomo una decision 
        const decisionMade = Math.abs(pullDeltaX) >= DECISION_THRESHOULD 

        if (decisionMade){
            const goRight = pullDeltaX >= 0
            const goleft = !goRight
            
            //add class acording to the desition 
            actualCard.classList.add(goRight ? 'go-right' : 'go-left')
            
         
        } else { 
            console.log('pensando....')
        }

    }
}


document.addEventListener('mousedown', startDrag)
document.addEventListener('touchstart', startDrag, { passive:true})