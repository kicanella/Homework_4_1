from selene.support.shared import browser
from selene import be, have


browser.open('https://qa.guru/')
browser.element('[id=" "]').should(be.blank).type(' ').press_enter()