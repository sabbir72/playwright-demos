describe('Automation', () => {
  it('Test', () => {
    cy.visit("https://demoqa.com/text-box")
    cy.findByPlaceholderText("Full Name",{"trim":true}).click()
    cy.findByPlaceholderText("Full Name",{"trim":true}).type("sabbir ")
    cy.findByPlaceholderText("name@example.com",{"trim":true}).click()
    cy.findByPlaceholderText("name@example.com",{"trim":true}).type("sabbir@gmail.com")
    cy.findByPlaceholderText("Current Address",{"trim":true}).click()
    cy.findByPlaceholderText("Current Address",{"trim":true}).type("Tongi")
    cy.get("#permanentAddress").click()
    cy.get("#permanentAddress").type("Kishoregonj")
    cy.findByRole("button",{"name":"Submit"}).click()
  })
})