
class Tina extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" })
    const wrapper = document.createElement("h6")

    wrapper.innerText = "Just a side chick, Tina."

    shadow.appendChild(wrapper)
  }
}

customElements.define('side-chick-tina', Tina)
