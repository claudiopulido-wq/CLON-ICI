import os

INDEX_FILE = "index.html"
STYLE_FILE = "css/style.css"

HTML_TO_INSERT = """
    <!-- Ask an Advisor Section -->
    <section class="ask-advisor-section" id="ask-advisor">
        <div class="ask-advisor-image"></div>
        <div class="ask-advisor-content">
            <h2>Ask an <span>Advisor</span></h2>
            <p>Not sure which program is best to achieve your goals? Let us help you build the best possible program for you!</p>
            
            <div class="quiz-container-box">
                <!-- Form Container -->
                <div id="quiz-container">
                    <div class="quiz-progress">
                        <span class="quiz-step-counter">1/7</span>
                        <div class="quiz-progress-bar">
                            <div class="quiz-progress-bar-fill" style="width: 0%;"></div>
                        </div>
                    </div>
                    
                    <form id="advisor-quiz">
                        <!-- Step 1 -->
                        <div class="quiz-step active" id="step-1">
                            <h3>What are you interested in?</h3>
                            <p class="subtitle">Pick as many as you like!</p>
                            <div class="quiz-options">
                                <label class="quiz-option"><input type="checkbox" name="interest" value="Mat Pilates"> Mat Pilates</label>
                                <label class="quiz-option"><input type="checkbox" name="interest" value="Barre"> Barre</label>
                                <label class="quiz-option"><input type="checkbox" name="interest" value="Sculpt & Burn"> Sculpt & Burn</label>
                                <label class="quiz-option"><input type="checkbox" name="interest" value="I'm not sure yet"> I'm not sure yet</label>
                            </div>
                            <div class="quiz-actions" style="justify-content: flex-end;">
                                <button type="button" class="btn-next">Next →</button>
                            </div>
                        </div>
                        
                        <!-- Step 2 -->
                        <div class="quiz-step" id="step-2">
                            <h3>What's your experience level?</h3>
                            <div class="quiz-options">
                                <label class="quiz-option"><input type="radio" name="experience" value="I'm completely new"> I'm completely new</label>
                                <label class="quiz-option"><input type="radio" name="experience" value="I've taken classes before"> I've taken classes before</label>
                                <label class="quiz-option"><input type="radio" name="experience" value="I already teach classes"> I already teach classes</label>
                                <label class="quiz-option"><input type="radio" name="experience" value="I've been teaching for several years"> I've been teaching for several years</label>
                            </div>
                            <div class="quiz-actions">
                                <button type="button" class="btn-back">← Back</button>
                                <button type="button" class="btn-next">Next →</button>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div class="quiz-step" id="step-3">
                            <h3>What best describes your goal?</h3>
                            <div class="quiz-options">
                                <label class="quiz-option"><input type="radio" name="goal" value="Start teaching professionally"> Start teaching professionally</label>
                                <label class="quiz-option"><input type="radio" name="goal" value="Add another certification"> Add another certification</label>
                                <label class="quiz-option"><input type="radio" name="goal" value="Validate my current experience"> Validate my current experience</label>
                                <label class="quiz-option"><input type="radio" name="goal" value="Open my own studio"> Open my own studio</label>
                            </div>
                            <div class="quiz-actions">
                                <button type="button" class="btn-back">← Back</button>
                                <button type="button" class="btn-next">Next →</button>
                            </div>
                        </div>

                        <!-- Step 4 -->
                        <div class="quiz-step" id="step-4">
                            <h3>Which learning experience fits you best?</h3>
                            <div class="quiz-options">
                                <label class="quiz-option"><input type="radio" name="learning" value="Weekend in-person certification"> Weekend in-person certification</label>
                                <label class="quiz-option"><input type="radio" name="learning" value="Distance-based competency assessment"> Distance-based competency assessment</label>
                                <label class="quiz-option"><input type="radio" name="learning" value="I'm open to either option"> I'm open to either option</label>
                                <label class="quiz-option"><input type="radio" name="learning" value="I'm not sure"> I'm not sure</label>
                            </div>
                            <div class="quiz-actions">
                                <button type="button" class="btn-back">← Back</button>
                                <button type="button" class="btn-next">Next →</button>
                            </div>
                        </div>

                        <!-- Step 5 -->
                        <div class="quiz-step" id="step-5">
                            <h3>Where should we send your personalized recommendation?</h3>
                            <div class="quiz-inputs">
                                <label>Email <span>*</span></label>
                                <input type="email" name="email" required placeholder="your.email@example.com">
                            </div>
                            <div class="quiz-actions">
                                <button type="button" class="btn-back">← Back</button>
                                <button type="button" class="btn-next">Next →</button>
                            </div>
                        </div>

                        <!-- Step 6 -->
                        <div class="quiz-step" id="step-6">
                            <h3>Tell us your name</h3>
                            <div class="quiz-inputs">
                                <label>First Name <span>*</span></label>
                                <input type="text" id="quiz-fname" name="fname" required placeholder="First Name">
                                <label>Last Name <span>*</span></label>
                                <input type="text" name="lname" required placeholder="Last Name">
                            </div>
                            <div class="quiz-actions">
                                <button type="button" class="btn-back">← Back</button>
                                <button type="button" class="btn-next">Next →</button>
                            </div>
                        </div>

                        <!-- Step 7 -->
                        <div class="quiz-step" id="step-7">
                            <h3>What's the best number to reach you?</h3>
                            <div class="quiz-inputs">
                                <label>Phone Number <span>*</span></label>
                                <input type="tel" name="phone" required placeholder="+1 234 567 8900">
                                
                                <label style="font-weight: normal; font-size: 0.8rem; margin-top: 10px; display: flex; align-items: start; gap: 10px;">
                                    <input type="checkbox" name="agree" style="margin-top: 3px;">
                                    I agree to receive updates regarding my certification.
                                </label>
                            </div>
                            <div class="quiz-actions">
                                <button type="button" class="btn-back">← Back</button>
                                <button type="button" class="btn-submit">Get My Recommendation →</button>
                            </div>
                        </div>
                    </form>
                </div>

                <!-- Results Container -->
                <div id="results-container">
                    <!-- RESULT 1 -->
                    <div class="result-card" id="result-1">
                        <h3>Mat Pilates Certification</h3>
                        <p class="result-greeting">Hi [First Name], your evaluation kit is on its way. Based on your responses, we recommend our Mat Pilates Certification.</p>
                        <h4>Your Personalized Path: Mat Pilates Certification</h4>
                        <div class="result-why">
                            <p style="font-weight: bold; margin-bottom: 5px;">Why this fits you</p>
                            <ul>
                                <li>Perfect foundation for new instructors.</li>
                                <li>Learn movement, technique, and teaching fundamentals.</li>
                                <li>Internationally recognized certification.</li>
                                <li>Build confidence before leading your own classes.</li>
                            </ul>
                        </div>
                        <div class="result-buttons">
                            <a href="#" class="btn-outline">Learn More</a>
                            <a href="#" class="btn-submit">Enroll Now</a>
                        </div>
                    </div>
                    
                    <!-- RESULT 2 -->
                    <div class="result-card" id="result-2">
                        <h3>Barre Certification</h3>
                        <p class="result-greeting">Hi [First Name], your evaluation kit is on its way. Based on your responses, we recommend our Barre Certification.</p>
                        <h4>Your Personalized Path: Barre Certification</h4>
                        <div class="result-why">
                            <p style="font-weight: bold; margin-bottom: 5px;">Why this fits you</p>
                            <ul>
                                <li>Ideal if you enjoy rhythm, music, and fluid movement.</li>
                                <li>Perfect addition to your fitness career.</li>
                                <li>Internationally recognized certification.</li>
                                <li>Great for boutique studios and group fitness.</li>
                            </ul>
                        </div>
                        <div class="result-buttons">
                            <a href="#" class="btn-outline">Learn More</a>
                            <a href="#" class="btn-submit">Enroll Now</a>
                        </div>
                    </div>

                    <!-- RESULT 3 -->
                    <div class="result-card" id="result-3">
                        <h3>Sculpt & Burn Certification</h3>
                        <p class="result-greeting">Hi [First Name], your evaluation kit is on its way. Based on your responses, we recommend our Sculpt & Burn Certification.</p>
                        <h4>Your Personalized Path: Sculpt & Burn Certification</h4>
                        <div class="result-why">
                            <p style="font-weight: bold; margin-bottom: 5px;">Why this fits you</p>
                            <ul>
                                <li>High-energy functional workouts.</li>
                                <li>Great for coaches looking to diversify.</li>
                                <li>Fast-growing training methodology.</li>
                                <li>International certification.</li>
                            </ul>
                        </div>
                        <div class="result-buttons">
                            <a href="#" class="btn-outline">Learn More</a>
                            <a href="#" class="btn-submit">Enroll Now</a>
                        </div>
                    </div>

                    <!-- RESULT 4 -->
                    <div class="result-card" id="result-4">
                        <h3>Triple Certification Bundle</h3>
                        <p class="result-greeting">Hi [First Name], your evaluation kit is on its way. Based on your responses, we recommend our Triple Certification Bundle.</p>
                        <h4>Your Personalized Path: Triple Certification Bundle</h4>
                        <div class="result-why">
                            <p style="font-weight: bold; margin-bottom: 5px;">Why this fits you</p>
                            <ul>
                                <li>Master Mat Pilates, Barre, and Sculpt & Burn.</li>
                                <li>Save compared to enrolling separately.</li>
                                <li>Expand your coaching opportunities.</li>
                                <li>Become a more versatile instructor.</li>
                            </ul>
                        </div>
                        <div class="result-buttons">
                            <a href="#" class="btn-outline">Learn More</a>
                            <a href="#" class="btn-submit">Enroll Now</a>
                        </div>
                    </div>

                    <!-- RESULT 5 -->
                    <div class="result-card" id="result-5">
                        <h3>Competency Assessment</h3>
                        <p class="result-greeting">Hi [First Name], your evaluation kit is on its way. Based on your responses, we recommend our Competency Assessment Pathway.</p>
                        <h4>Your Personalized Path: Competency Assessment</h4>
                        <div class="result-why">
                            <p style="font-weight: bold; margin-bottom: 5px;">Why this fits you</p>
                            <ul>
                                <li>Designed for experienced instructors.</li>
                                <li>Validate your skills without taking the full certification.</li>
                                <li>Complete a theory and practical assessment.</li>
                                <li>Earn an internationally recognized certification.</li>
                            </ul>
                        </div>
                        <div class="result-buttons">
                            <a href="#" class="btn-outline">Learn More</a>
                            <a href="#" class="btn-submit">Start Assessment</a>
                        </div>
                    </div>

                    <!-- RESULT 6 -->
                    <div class="result-card" id="result-6">
                        <h3>Personalized Advisor Recommendation</h3>
                        <p class="result-greeting">Hi [First Name], your evaluation kit is on its way. Based on your responses, we recommend speaking with one of our advisors.</p>
                        <h4>Your Personalized Path: Advisor Consultation</h4>
                        <div class="result-why">
                            <p style="font-weight: bold; margin-bottom: 5px;">Why this fits you</p>
                            <ul>
                                <li>You're exploring multiple options.</li>
                                <li>We'll help you compare every certification pathway.</li>
                                <li>Get personalized guidance based on your goals.</li>
                                <li>Find the certification that best fits your experience.</li>
                            </ul>
                        </div>
                        <div class="result-buttons">
                            <a href="#" class="btn-submit">Talk to an Advisor</a>
                            <a href="#" class="btn-outline">WhatsApp</a>
                        </div>
                    </div>

                    <div class="btn-restart-wrap">
                        <a href="#" id="btn-restart">Take the quiz again</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

CSS_TO_APPEND = """
/* Ask an Advisor Section */
.ask-advisor-section {
  display: flex;
  background-color: var(--color-white);
  padding: 4rem 0;
  min-height: 80vh;
}

.ask-advisor-image {
  flex: 1;
  background-image: url('../assets/block2.jpg');
  background-size: cover;
  background-position: center;
  position: relative;
  /* Trying a brush stroke clipping mask using SVG data uri (rough brush shape) */
  -webkit-mask-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><path d="M20,100 Q80,20 180,90 T20,100" fill="black" stroke="black" stroke-width="40" stroke-linecap="round"/></svg>');
  mask-image: url('data:image/svg+xml;utf8,<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"><path d="M20,100 Q80,20 180,90 T20,100" fill="black" stroke="black" stroke-width="40" stroke-linecap="round"/></svg>');
  -webkit-mask-size: 80%;
  -webkit-mask-repeat: no-repeat;
  -webkit-mask-position: center;
  mask-size: 80%;
  mask-repeat: no-repeat;
  mask-position: center;
}

/* Yellow brush under */
.ask-advisor-image::before {
  content: '';
  position: absolute;
  top: 30%;
  left: 5%;
  width: 90%;
  height: 40%;
  background: var(--color-secondary);
  border-radius: 50% 50% 30% 70% / 60% 40% 70% 40%;
  transform: rotate(-10deg);
  z-index: -1;
}

.ask-advisor-content {
  flex: 1;
  padding: 2rem 5%;
  max-width: 600px;
}

.ask-advisor-content h2 {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 0.5rem;
  line-height: 1.1;
}

.ask-advisor-content h2 span {
  color: var(--color-primary);
  font-style: italic;
  font-family: 'Montserrat', sans-serif; /* or a script font if available */
}

.quiz-container-box {
  background: var(--color-white);
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  border: 1px solid #eee;
  padding: 2rem;
  margin-top: 2rem;
}

.quiz-progress {
  display: flex;
  align-items: center;
  margin-bottom: 2rem;
}

.quiz-step-counter {
  font-size: 0.8rem;
  font-weight: 600;
  color: #666;
  margin-right: 1rem;
}

.quiz-progress-bar {
  flex: 1;
  height: 4px;
  background: #eee;
  border-radius: 2px;
  position: relative;
}

.quiz-progress-bar-fill {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  background: var(--color-secondary);
  border-radius: 2px;
  width: 0%;
  transition: width 0.3s ease;
}

.quiz-step {
  display: none;
}
.quiz-step.active {
  display: block;
  animation: fadeIn 0.4s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.quiz-step h3 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
  text-align: center;
  font-weight: 700;
}

.quiz-step p.subtitle {
  text-align: center;
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.quiz-option {
  border: 1px solid #ddd;
  border-radius: 25px;
  padding: 10px 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  transition: all 0.2s;
  font-size: 0.95rem;
}

.quiz-option:hover {
  background-color: #f9f9f9;
}

.quiz-option.selected {
  background-color: var(--color-secondary);
  border-color: var(--color-secondary);
  color: #000;
  font-weight: 600;
}

.quiz-option input {
  margin-right: 15px;
  cursor: pointer;
}

.quiz-inputs {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.quiz-inputs label {
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: -0.5rem;
}
.quiz-inputs label span { color: red; }

.quiz-inputs input[type="text"],
.quiz-inputs input[type="email"],
.quiz-inputs input[type="tel"] {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.quiz-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}

.btn-back {
  background: transparent;
  border: 1px solid #ddd;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
}

.btn-next, .btn-submit {
  background: var(--color-secondary);
  color: #000;
  border: none;
  padding: 10px 30px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 700;
  margin-left: auto;
}

.btn-submit {
  background: var(--color-primary);
  color: var(--color-white);
}

/* Results */
#results-container {
  display: none;
}

.result-card {
  display: none;
}

.result-card h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.result-card p.result-greeting {
  font-size: 0.95rem;
  color: #444;
  margin-bottom: 20px;
}

.result-card h4 {
  color: var(--color-dark);
  font-size: 1.1rem;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
  margin-bottom: 10px;
}

.result-card ul {
  list-style: none;
  margin: 1rem 0;
  padding: 0;
}

.result-card ul li {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.result-card ul li::before {
  content: '✓';
  color: #2e8b57;
  margin-right: 8px;
  font-weight: bold;
}

.result-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.btn-outline {
  border: 2px solid var(--color-primary);
  color: var(--color-primary);
  background: transparent;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  font-weight: 600;
  display: inline-block;
  text-align: center;
}

.btn-submit {
  display: inline-block;
  text-align: center;
  text-decoration: none;
}

.btn-restart-wrap {
  text-align: center;
  margin-top: 2rem;
}

.btn-restart-wrap a {
  color: var(--color-secondary);
  text-decoration: underline;
  font-size: 0.9rem;
  font-weight: 600;
}

@media (max-width: 900px) {
  .ask-advisor-section {
    flex-direction: column;
  }
  .ask-advisor-image {
    min-height: 350px;
    -webkit-mask-size: 100%;
    mask-size: 100%;
  }
  .ask-advisor-content {
    max-width: 100%;
  }
}
"""

def update_index():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    # Insert HTML before <!-- Footer -->
    html = html.replace('<!-- Footer -->', HTML_TO_INSERT + '\n    <!-- Footer -->')

    # Insert <script src="js/quiz.js"></script> before </body>
    if '<script src="js/quiz.js"></script>' not in html:
        html = html.replace('</body>', '    <script src="js/quiz.js"></script>\n</body>')

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)

def update_css():
    with open(STYLE_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + CSS_TO_APPEND)

if __name__ == "__main__":
    update_index()
    update_css()
    print("Quiz section injected successfully.")
