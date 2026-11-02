/**
 * Scam or Smart Deal? | Investment Hype Awareness
 * Community Engagement Project (CEP) • MIT Chhatrapati Sambhajinagar
 * Academic Year 2026–27
 * 
 * Vanilla JavaScript application logic:
 * - Mobile Navigation Toggle & Accessible Keyboard Handling
 * - Interactive Scam Spotter Scenario Simulation
 * - In-Memory Quick Awareness Quiz Engine with Accessible Live Regions
 * - Scrollspy & Floating Back-to-Top Button
 * - Zero Backend, Zero Persistent Storage, Zero Data Collection
 */

(function () {
  'use strict';

  /* ==========================================================================
     1. Navigation & Mobile Menu Handler
     ========================================================================== */
  const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
  const primaryNav = document.getElementById('primary-navigation');
  const navLinks = document.querySelectorAll('.nav-link');
  const siteHeader = document.querySelector('.site-header');

  if (mobileNavToggle && primaryNav) {
    mobileNavToggle.addEventListener('click', function () {
      const isExpanded = mobileNavToggle.getAttribute('aria-expanded') === 'true';
      mobileNavToggle.setAttribute('aria-expanded', !isExpanded);
      primaryNav.classList.toggle('is-open', !isExpanded);
    });

    // Close mobile nav when clicking a regular page link (not dropdown toggles)
    navLinks.forEach(function (link) {
      link.addEventListener('click', function () {
        if (link.classList.contains('dropdown-toggle')) {
          return;
        }
        if (primaryNav.classList.contains('is-open')) {
          primaryNav.classList.remove('is-open');
          mobileNavToggle.setAttribute('aria-expanded', 'false');
        }
      });
    });

    // Close mobile nav when clicking a dropdown item link
    const dropdownLinks = document.querySelectorAll('.dropdown-item');
    dropdownLinks.forEach(function (item) {
      item.addEventListener('click', function () {
        if (primaryNav.classList.contains('is-open')) {
          primaryNav.classList.remove('is-open');
          mobileNavToggle.setAttribute('aria-expanded', 'false');
        }
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && primaryNav.classList.contains('is-open')) {
        primaryNav.classList.remove('is-open');
        mobileNavToggle.setAttribute('aria-expanded', 'false');
        mobileNavToggle.focus();
      }
    });
  }

  /* Dropdown Toggle Handling */
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(function (toggle) {
    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      const parent = this.closest('.has-dropdown');
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      
      // Close any other open dropdowns
      document.querySelectorAll('.has-dropdown').forEach(item => {
        if (item !== parent) {
          item.classList.remove('is-active');
          const btn = item.querySelector('.dropdown-toggle');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        }
      });

      this.setAttribute('aria-expanded', !isExpanded);
      if (parent) {
        parent.classList.toggle('is-active', !isExpanded);
      }
    });
  });

  // Close dropdowns on outside click
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-dropdown')) {
      document.querySelectorAll('.has-dropdown').forEach(item => {
        item.classList.remove('is-active');
        const btn = item.querySelector('.dropdown-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Close dropdowns on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.has-dropdown').forEach(item => {
        item.classList.remove('is-active');
        const btn = item.querySelector('.dropdown-toggle');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
    }
  });

  /* Header Shadow on Scroll */
  window.addEventListener('scroll', function () {
    if (window.scrollY > 20) {
      siteHeader.classList.add('scrolled');
    } else {
      siteHeader.classList.remove('scrolled');
    }
  }, { passive: true });


  /* ==========================================================================
     2. Floating Back to Top Button & Scrollspy
     ========================================================================== */
  const backToTopBtn = document.getElementById('floating-back-to-top');

  window.addEventListener('scroll', function () {
    if (window.scrollY > 400) {
      if (backToTopBtn) backToTopBtn.hidden = false;
    } else {
      if (backToTopBtn) backToTopBtn.hidden = true;
    }
    updateScrollspy();
  }, { passive: true });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  function updateScrollspy() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPosition = window.scrollY + 120;

    sections.forEach(function (section) {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      const id = section.getAttribute('id');
      const matchingLink = document.querySelector(`.nav-link[href="#${id}"]`);

      if (matchingLink) {
        if (scrollPosition >= top && scrollPosition < top + height) {
          navLinks.forEach(l => l.classList.remove('active'));
          matchingLink.classList.add('active');
        }
      }
    });
  }


  /* ==========================================================================
     3. Scam Spotter Challenge: Interactive Scenario Engine
     ========================================================================== */
  const scenarioExplanations = {
    1: {
      a: {
        isSafe: false,
        header: '⚠️ Warning Signs Found: Artificial Urgency & Guaranteed Profits',
        text: 'Joining under a midnight deadline means making an unverified decision driven by fear of missing out (FOMO). In the securities market, no regulated algorithm or entity can promise a fixed 5% daily return or zero loss. Such guarantees violate core financial realities.',
        takeaway: 'Key takeaway: Urgency is designed to prevent verification. Pause and step back.'
      },
      b: {
        isSafe: true,
        header: '🛡️ Safer Next Step: Spotting Deception & Pausing',
        text: 'Excellent decision. You recognized the double warning sign: impossible "zero-loss guaranteed daily returns" coupled with a high-pressure countdown clock. Real securities markets fluctuate constantly, and no genuine investment opportunity expires at midnight.',
        takeaway: 'Key takeaway: Legitimate investments do not demand rushed decisions.'
      },
      c: {
        isSafe: false,
        header: '⚠️ Caution: Scammers Readily Fabricate Proof',
        text: 'Direct messaging a scam account gives the fraudster an opportunity to use personalized social engineering. Digital tax statements, audit stamps, and certificates are easily forged. Independent verification through SEBI\'s public portal is the only reliable check.',
        takeaway: 'Key takeaway: Never ask the promoter to verify themselves. Check official sources independently.'
      }
    },
    2: {
      a: {
        isSafe: false,
        header: '⚠️ Warning Signs Found: Follower Illusion & Selective Proof',
        text: 'Large follower counts and blue checkmarks can be purchased cheaply online or acquired through non-financial content. Selected profit screenshots hide massive losses and are trivially fabricated in graphic software. Never pay for unregistered stock tips based on social popularity.',
        takeaway: 'Key takeaway: Social media popularity is not proof of regulatory authorization or competence.'
      },
      b: {
        isSafe: false,
        header: '⚠️ Warning Signs Found: False Sense of Payment Security',
        text: 'Paying via UPI does not make an unregistered advisory service legitimate or safe. Scammers frequently cycle through third-party mule bank accounts or disposable merchant IDs. Once money is transferred voluntarily, reversal is complex and not guaranteed.',
        takeaway: 'Key takeaway: The payment method does not validate the seller.'
      },
      c: {
        isSafe: true,
        header: '🛡️ Safer Next Step: Demanding Independent Regulatory Verification',
        text: 'Correct approach. Under Indian law, anyone providing stock trading calls or charging fees for investment advice must be registered with SEBI as an Investment Adviser (IA) or Research Analyst (RA). Check their official SEBI registration number independently on investor.sebi.gov.in.',
        takeaway: 'Key takeaway: Always verify registration on the regulator’s directory, not from the promoter’s link.'
      }
    },
    3: {
      a: {
        isSafe: true,
        header: '🛡️ Safer Next Step: Rejecting Sideloaded APKs & Third-Party Payments',
        text: 'Outstanding choice. Sideloading direct APK packages circumvents essential app-store security reviews. Fraudulent apps simulate high returns while secretly stealing your deposit and accessing sensitive phone data. Legitimate Indian brokers are registered members of NSE/BSE and SEBI.',
        takeaway: 'Key takeaway: Never install APK files sent in chat groups; never deposit funds into personal UPI IDs.'
      },
      b: {
        isSafe: false,
        header: '🚨 Critical Danger: Incognito Mode Offers No OS Protection',
        text: 'Private/incognito browsing only prevents browser history and cookies from saving locally; it provides ZERO defense against an installed malicious APK. Once installed on your operating system, rogue apps can intercept SMS messages (including bank OTPs) and steal credentials.',
        takeaway: 'Key takeaway: Private browsing does not sandbox installed applications.'
      },
      c: {
        isSafe: false,
        header: '⚠️ Warning Signs Found: The "Small Test" Trap',
        text: 'Sending a small amount (like ₹1,000) directly exposes your financial details and plays into the scammer’s playbook. Scammers frequently allow users to withdraw small initial amounts to build false trust before convincing them to deposit life savings.',
        takeaway: 'Key takeaway: Never test an unverified scheme with real money.'
      }
    },
    4: {
      a: {
        isSafe: false,
        header: '🚨 Critical Trap: The Advance Fee Extortion Cycle',
        text: 'Paying the ₹36,750 will not release your funds. The ₹2,45,000 balance shown on the screen is purely fictional. Once you pay the fee, the scammers will invent new requirements ("anti-money laundering fee", "foreign exchange clearance penalty") until you realize you are being scammed.',
        takeaway: 'Key takeaway: Never pay money to withdraw your own money.'
      },
      b: {
        isSafe: false,
        header: '⚠️ Warning Signs Found: The Balance Does Not Exist',
        text: 'Offering to deduct the fee from the profits will simply prompt the scammers to invent reasons why external funds are required. The numbers on the screen were created by the app developers; there are no actual profits or securities held in your name.',
        takeaway: 'Key takeaway: Scammers demand fresh liquid funds because displayed balances are fictional.'
      },
      c: {
        isSafe: true,
        header: '🛡️ Safer Next Step: Immediate Stop & Official Reporting',
        text: 'Correct action. Genuine SEBI-regulated brokers and mutual fund platforms deduct applicable taxes (like Securities Transaction Tax) and brokerage automatically from your trading balance. They NEVER ask you to deposit outside funds to release your balance. Cease communication and report to 1930 immediately.',
        takeaway: 'Key takeaway: Fee demands to unlock withdrawals match the classic fake app scam pattern.'
      }
    }
  };

  const choiceButtons = document.querySelectorAll('.btn-choice');

  choiceButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      const scenarioId = this.getAttribute('data-scenario');
      const choiceKey = this.getAttribute('data-choice');
      const scenarioCard = document.getElementById(`scenario-${scenarioId}`);
      const feedbackBox = document.getElementById(`feedback-scenario-${scenarioId}`);

      if (!scenarioExplanations[scenarioId] || !scenarioExplanations[scenarioId][choiceKey]) {
        return;
      }

      const explanation = scenarioExplanations[scenarioId][choiceKey];

      // Update button styling within this scenario
      const siblingButtons = scenarioCard.querySelectorAll('.btn-choice');
      siblingButtons.forEach(btn => {
        btn.classList.remove('choice-selected-safe', 'choice-selected-risky');
      });

      if (explanation.isSafe) {
        this.classList.add('choice-selected-safe');
      } else {
        this.classList.add('choice-selected-risky');
      }

      // Populate feedback box
      feedbackBox.className = 'scenario-feedback ' + (explanation.isSafe ? 'feedback-safe' : 'feedback-risky');
      feedbackBox.innerHTML = `
        <div class="feedback-header">
          ${explanation.header}
        </div>
        <p class="feedback-text">${explanation.text}</p>
        <div class="feedback-takeaway">
          <strong>Summary:</strong> ${explanation.takeaway}
        </div>
      `;
      feedbackBox.hidden = false;
    });
  });


  /* ==========================================================================
     4. Quick Awareness Quiz Engine (In-Memory Only)
     ========================================================================== */
  const quizQuestions = [
    {
      question: "A social-media trading promoter promises 'Guaranteed 10% monthly returns from stock options with zero risk.' How should you evaluate this?",
      options: [
        { label: "A", text: "It is a reliable opportunity if the promoter has over 50,000 followers.", isCorrect: false },
        { label: "B", text: "It is a major red flag; all securities-market investments carry risk and no entity can guarantee profits.", isCorrect: true },
        { label: "C", text: "It is completely legitimate as long as the promoter offers a money-back trial.", isCorrect: false }
      ],
      explanation: "All securities-market investments carry inherent risk. SEBI repeatedly warns that promises of assured, guaranteed, or unusually high fixed returns are typical hallmarks of financial scams."
    },
    {
      question: "A messaging group announcement says: 'Only 3 VIP slots left! Offer expires in 20 minutes! Transfer funds now to join.' What tactic is this?",
      options: [
        { label: "A", text: "Standard professional scheduling required by stock exchanges.", isCorrect: false },
        { label: "B", text: "High-pressure artificial urgency designed to bypass critical thinking and verification.", isCorrect: true },
        { label: "C", text: "A routine regulatory quota for retail stock trading.", isCorrect: false }
      ],
      explanation: "High-pressure urgency ('act now', 'limited seats', 'expires at midnight') tries to rush you into an emotional decision before you can pause, verify registration, or consult trusted sources."
    },
    {
      question: "Why should profit screenshots shared in a chat channel NOT be accepted as verification of success?",
      options: [
        { label: "A", text: "Because screenshots are easily fabricated, selectively chosen, or taken from risk-free demo accounts.", isCorrect: true },
        { label: "B", text: "Because SEBI regulations require screenshots to include the user's Aadhaar number.", isCorrect: false },
        { label: "C", text: "Because stock market profits cannot be photographed under copyright law.", isCorrect: false }
      ],
      explanation: "Digital images and edited clips are trivial to create or doctor. Promoters routinely showcase winning demo trades while concealing significant real-money losses."
    },
    {
      question: "What is the safest action if an administrator in a Telegram group sends an APK file download link for an 'exclusive institutional trading app'?",
      options: [
        { label: "A", text: "Install it and test it with a disposable password first.", isCorrect: false },
        { label: "B", text: "Do not install it. Sideloaded APKs bypass security checks and can simulate fake profits; verify platforms via official exchange listings.", isCorrect: true },
        { label: "C", text: "Download it only if your phone has antivirus software installed.", isCorrect: false }
      ],
      explanation: "Unsolicited APK download links bypass platform security checks. Scammers control the software to show simulated balances and can steal credentials or intercept OTPs."
    },
    {
      question: "An investment platform displays substantial profits but insists you must deposit a 15% upfront 'tax clearance fee' before withdrawing. What does this indicate?",
      options: [
        { label: "A", text: "A standard legal requirement for all Indian retail stock accounts.", isCorrect: false },
        { label: "B", text: "A classic fake trading app extortion trap; genuine brokers deduct statutory taxes directly from your account balance.", isCorrect: true },
        { label: "C", text: "The platform is offering a legal rebate on capital gains tax.", isCorrect: false }
      ],
      explanation: "Legitimate regulated brokers automatically deduct applicable taxes (STT/TDS) and charges from your balance. Demanding outside upfront deposits to release funds is an extortion trap."
    },
    {
      question: "If an individual in India suspects they have transferred money to a cyber financial scam, what is the official emergency reporting route?",
      options: [
        { label: "A", text: "Post the loss on social media to enlist independent recovery hackers.", isCorrect: false },
        { label: "B", text: "Dial 1930 immediately or lodge an incident at cybercrime.gov.in, understanding that reporting does not guarantee fund recovery.", isCorrect: true },
        { label: "C", text: "Wait 30 days to see if the trading platform completes the settlement.", isCorrect: false }
      ],
      explanation: "The official National Cyber Financial Fraud Helpline is 1930, linked to cybercrime.gov.in. Calling promptly gives authorities the best opportunity to freeze funds, though recovery is never guaranteed."
    }
  ];

  let currentQuestionIndex = 0;
  let userScore = 0;
  let answeredQuestions = {};

  const questionNumberEl = document.getElementById('quiz-question-number');
  const totalQuestionsEl = document.getElementById('quiz-total-questions');
  const progressFillEl = document.getElementById('quiz-progress-fill');
  const questionTitleEl = document.getElementById('quiz-question-title');
  const optionsContainerEl = document.getElementById('quiz-options');
  const feedbackEl = document.getElementById('quiz-feedback');
  const nextBtn = document.getElementById('quiz-next-btn');
  const questionBodyEl = document.getElementById('quiz-question-body');
  const resultsContainerEl = document.getElementById('quiz-results');
  const resultsScoreEl = document.getElementById('results-score-text');
  const resultsMsgEl = document.getElementById('results-message-text');
  const retryBtn = document.getElementById('quiz-retry-btn');

  function initQuiz() {
    if (!questionTitleEl || !optionsContainerEl) return;
    currentQuestionIndex = 0;
    userScore = 0;
    answeredQuestions = {};
    if (totalQuestionsEl) totalQuestionsEl.textContent = quizQuestions.length;
    if (resultsContainerEl) resultsContainerEl.hidden = true;
    if (questionBodyEl) questionBodyEl.hidden = false;
    renderQuestion(currentQuestionIndex);
  }

  function renderQuestion(index) {
    if (!questionTitleEl || !optionsContainerEl) return;

    const q = quizQuestions[index];
    questionNumberEl.textContent = `Question ${index + 1}`;
    
    // Update progress bar
    const progressPercent = ((index + 1) / quizQuestions.length) * 100;
    progressFillEl.style.width = `${progressPercent}%`;
    progressFillEl.parentElement.setAttribute('aria-valuenow', index + 1);

    questionTitleEl.textContent = q.question;
    optionsContainerEl.innerHTML = '';
    feedbackEl.hidden = true;
    feedbackEl.className = 'quiz-feedback';
    feedbackEl.innerHTML = '';
    nextBtn.style.display = 'none';

    // Render options
    q.options.forEach(function (opt, optIndex) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'quiz-option-btn';
      btn.setAttribute('data-index', optIndex);
      btn.innerHTML = `
        <span class="option-badge" aria-hidden="true">${opt.label}</span>
        <span class="option-text">${opt.text}</span>
      `;

      btn.addEventListener('click', function () {
        handleOptionSelect(index, optIndex);
      });

      optionsContainerEl.appendChild(btn);
    });
  }

  function handleOptionSelect(qIndex, selectedOptIndex) {
    if (answeredQuestions[qIndex] !== undefined) return; // Prevent multiple answers

    answeredQuestions[qIndex] = selectedOptIndex;
    const q = quizQuestions[qIndex];
    const selectedOpt = q.options[selectedOptIndex];
    const isCorrect = selectedOpt.isCorrect;

    if (isCorrect) {
      userScore++;
    }

    // Update buttons
    const allOptionBtns = optionsContainerEl.querySelectorAll('.quiz-option-btn');
    allOptionBtns.forEach(function (btn, idx) {
      btn.disabled = true;
      if (q.options[idx].isCorrect) {
        btn.classList.add('selected-correct');
      } else if (idx === selectedOptIndex && !isCorrect) {
        btn.classList.add('selected-incorrect');
      }
    });

    // Show feedback
    feedbackEl.className = 'quiz-feedback ' + (isCorrect ? 'quiz-feedback-correct' : 'quiz-feedback-incorrect');
    feedbackEl.innerHTML = `
      <div class="quiz-feedback-title">${isCorrect ? '✓ Correct Answer' : '⚠️ Learning Opportunity'}</div>
      <p class="quiz-feedback-body">${q.explanation}</p>
    `;
    feedbackEl.hidden = false;

    // Show next or finish button
    if (qIndex < quizQuestions.length - 1) {
      nextBtn.textContent = 'Next Question';
      nextBtn.style.display = 'inline-flex';
    } else {
      nextBtn.textContent = 'View Final Results';
      nextBtn.style.display = 'inline-flex';
    }
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', function () {
      if (currentQuestionIndex < quizQuestions.length - 1) {
        currentQuestionIndex++;
        renderQuestion(currentQuestionIndex);
      } else {
        showQuizResults();
      }
    });
  }

  function showQuizResults() {
    questionBodyEl.hidden = true;
    nextBtn.style.display = 'none';
    resultsContainerEl.hidden = false;

    resultsScoreEl.textContent = `You scored ${userScore} out of ${quizQuestions.length}`;

    if (userScore === quizQuestions.length) {
      resultsMsgEl.textContent = 'Outstanding! You demonstrated a complete understanding of critical investor red flags, verification requirements, and official emergency reporting pathways.';
    } else if (userScore >= 4) {
      resultsMsgEl.textContent = 'Good awareness! You recognized most major deception techniques. Review the red flags above to reinforce your verification habits.';
    } else {
      resultsMsgEl.textContent = 'Helpful learning session! Financial scams use sophisticated psychological tactics. Take a moment to review the 6 Red Flags and the Fake App lifecycle above.';
    }
  }

  if (retryBtn) {
    retryBtn.addEventListener('click', function () {
      initQuiz();
    });
  }

  // Initialize Quiz on page load if elements are present
  if (questionTitleEl && optionsContainerEl) {
    initQuiz();
  }

})();

