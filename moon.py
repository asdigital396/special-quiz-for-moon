<script>
    let correctAnswers = 0;

    function nextStep(stepNumber, answer) {
        if(stepNumber === 1 && answer === 'blue') { // সঠিক উত্তর চেক করা
            correctAnswers++;
        }

        document.getElementById('step' + stepNumber).classList.remove('active');
        let nextStepElement = document.getElementById('step' + (stepNumber + 1));
        if(nextStepElement) {
            nextStepElement.classList.add('active');
        } else if (correctAnswers === 1) { // সব উত্তর সঠিক হলে শুভেচ্ছা দেখানো
            document.getElementById('birthdayWish').classList.add('active');
        } else {
            document.getElementById('tryAgain').classList.add('active');
        }
    }
</script>
