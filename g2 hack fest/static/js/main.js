// Main JavaScript file for the application

// Function to handle form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;

    const password = form.querySelector('input[name="password"]');
    const confirmPassword = form.querySelector('input[name="confirm_password"]');

    if (password && confirmPassword && password.value !== confirmPassword.value) {
        alert('Passwords do not match!');
        return false;
    }

    return true;
}

// Function to handle mood logging
function logMood(mood, triggers, cravings) {
    return fetch('/api/log-mood', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            mood: mood,
            triggers: triggers,
            cravings: cravings
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            showNotification('Mood logged successfully!', 'success');
            return true;
        } else {
            showNotification('Failed to log mood', 'error');
            return false;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('An error occurred', 'error');
        return false;
    });
}

// Function to get coping strategies
function getCopingStrategies() {
    return fetch('/api/get-coping-strategies')
        .then(response => response.json())
        .then(data => {
            return data.strategies;
        })
        .catch(error => {
            console.error('Error:', error);
            return [];
        });
}

// Function to get milestones
function getMilestones() {
    return fetch('/api/get-milestones')
        .then(response => response.json())
        .then(data => {
            return data.milestones;
        })
        .catch(error => {
            console.error('Error:', error);
            return [];
        });
}

// Function to show notifications
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this.id)) {
                e.preventDefault();
            }
        });
    });
}); 