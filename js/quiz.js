document.addEventListener('DOMContentLoaded', () => {
    const steps = document.querySelectorAll('.quiz-step');
    const nextBtns = document.querySelectorAll('.btn-next');
    const backBtns = document.querySelectorAll('.btn-back');
    const submitBtn = document.querySelector('.btn-submit');
    const progressBar = document.querySelector('.quiz-progress-bar-fill');
    const stepCounter = document.querySelector('.quiz-step-counter');
    const quizForm = document.getElementById('advisor-quiz');
    const quizContainer = document.getElementById('quiz-container');
    const resultsContainer = document.getElementById('results-container');
    const restartBtn = document.getElementById('btn-restart');
    
    let currentStep = 1;
    const totalSteps = 7;
    
    // Show current step
    function showStep(stepNumber) {
        steps.forEach(step => step.classList.remove('active'));
        document.getElementById(`step-${stepNumber}`).classList.add('active');
        
        // Update progress bar
        const progress = ((stepNumber - 1) / (totalSteps - 1)) * 100;
        progressBar.style.width = `${progress}%`;
        stepCounter.textContent = `${stepNumber}/${totalSteps}`;
    }
    
    // Validate current step
    function validateStep(stepNumber) {
        const step = document.getElementById(`step-${stepNumber}`);
        const inputs = step.querySelectorAll('input');
        
        if (inputs.length === 0) return true; // No inputs to validate
        
        const type = inputs[0].type;
        
        if (type === 'radio' || type === 'checkbox') {
            const checked = step.querySelectorAll('input:checked');
            if (checked.length === 0) {
                alert('Please select at least one option.');
                return false;
            }
        } else if (type === 'email' || type === 'text' || type === 'tel') {
            let isValid = true;
            inputs.forEach(input => {
                if (input.required && !input.value.trim()) {
                    isValid = false;
                }
            });
            if (!isValid) {
                alert('Please fill in all required fields.');
                return false;
            }
        }
        return true;
    }
    
    // Next Button Logic
    nextBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            if (validateStep(currentStep)) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });
    
    // Back Button Logic
    backBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            currentStep--;
            showStep(currentStep);
        });
    });
    
    // Form Submit Logic
    if (submitBtn) {
        submitBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (validateStep(currentStep)) {
                calculateResult();
            }
        });
    }
    
    // Selectable Option Styling
    const options = document.querySelectorAll('.quiz-option input');
    options.forEach(option => {
        option.addEventListener('change', function() {
            if (this.type === 'radio') {
                const name = this.name;
                document.querySelectorAll(`input[name="${name}"]`).forEach(radio => {
                    radio.closest('.quiz-option').classList.remove('selected');
                });
                this.closest('.quiz-option').classList.add('selected');
            } else if (this.type === 'checkbox') {
                if (this.checked) {
                    this.closest('.quiz-option').classList.add('selected');
                } else {
                    this.closest('.quiz-option').classList.remove('selected');
                }
            }
        });
    });
    
    // Logic for calculating results
    function calculateResult() {
        const step1 = Array.from(document.querySelectorAll('input[name="interest"]:checked')).map(cb => cb.value);
        const step2 = document.querySelector('input[name="experience"]:checked')?.value || "";
        const step3 = document.querySelector('input[name="goal"]:checked')?.value || "";
        const step4 = document.querySelector('input[name="learning"]:checked')?.value || "";
        const firstName = document.getElementById('quiz-fname').value;
        
        let resultId = 'result-6'; // Default Advisor
        
        if (step3 === "Validate my current experience" || step4 === "Distance-based competency assessment") {
            resultId = 'result-5'; // Competency
        } else if (step1.length > 1 || step3 === "Start teaching professionally") {
            resultId = 'result-4'; // Triple Bundle
        } else if (step1.length === 1) {
            if (step1[0] === "Mat Pilates") resultId = 'result-1';
            else if (step1[0] === "Barre") resultId = 'result-2';
            else if (step1[0] === "Sculpt & Burn") resultId = 'result-3';
            else resultId = 'result-6'; // Not sure
        }
        
        showResult(resultId, firstName);
    }
    
    function showResult(resultId, name) {
        quizContainer.style.display = 'none';
        resultsContainer.style.display = 'block';
        
        // Hide all results
        document.querySelectorAll('.result-card').forEach(card => card.style.display = 'none');
        
        // Show specific result
        const targetCard = document.getElementById(resultId);
        if (targetCard) {
            targetCard.style.display = 'block';
            // Inject name
            const greeting = targetCard.querySelector('.result-greeting');
            if (greeting) {
                greeting.innerHTML = greeting.innerHTML.replace('[First Name]', name);
            }
            
            // Send welcome email using the backend PHP script
            sendWelcomeEmail(resultId, targetCard, name);
        }
    }
    
    function sendWelcomeEmail(resultId, targetCard, name) {
        const emailInput = document.querySelector('input[name="email"]');
        if (!emailInput) return;
        
        const email = emailInput.value;
        const title = targetCard.querySelector('h3')?.textContent || 'Personalized Advisor Recommendation';
        const whyBullets = Array.from(targetCard.querySelectorAll('.result-why li')).map(li => li.textContent);
        
        fetch('send_email.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                fname: name,
                result_id: resultId,
                result_title: title,
                result_why: whyBullets
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Email status:', data);
        })
        .catch(err => {
            console.error('Error sending email:', err);
        });
    }
    
    // Restart Quiz
    if (restartBtn) {
        restartBtn.addEventListener('click', (e) => {
            e.preventDefault();
            quizForm.reset();
            document.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
            currentStep = 1;
            resultsContainer.style.display = 'none';
            quizContainer.style.display = 'block';
            showStep(currentStep);
            
            // Re-hide all names in greetings (hacky but works for demo)
            document.querySelectorAll('.result-greeting').forEach(el => {
                el.innerHTML = el.innerHTML.replace(/Hi .*?,/, 'Hi [First Name],');
            });
        });
    }
});
