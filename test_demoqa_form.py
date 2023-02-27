from selene.support.shared import browser
from selene import be, have


browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id="firstName"]').should(be.blank).type('Name Test').press_enter()
browser.element('[id="lastName"]').should(be.blank).type('Testovich').press_enter()
browser.element('[id="userEmail"]').should(be.blank).type('test@test.com').press_enter()
browser.element('[id="gender-radio-3"]').type(' ')
browser.element('[id="userNumber"]').should(be.blank).type('1234567890').press_enter()
browser.element('[id="hobbies-checkbox-2"]').type(' ')
browser.element('[id="currentAddress"]').should(be.blank).type('Test').press_enter()
browser.element('[class="modal-content"]').should(have.text('Thanks for submitting the form'))