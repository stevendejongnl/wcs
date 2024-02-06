
class Henk extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" })
    const wrapper = document.createElement("h1")

    wrapper.innerText = "Hello!, me Henk the men who in a wrapper can!"

    shadow.appendChild(wrapper)
  }
}


class HenksSideChick extends HTMLElement {
  connectedCallback() {
    const shadow = this.attachShadow({ mode: "open" })
    const wrapper = document.createElement("h3")

    wrapper.innerHTML = "<side-chick-tina></side-chick-tina>"

    shadow.appendChild(wrapper)
  }
}

customElements.define('henk-the-men', Henk)
customElements.define('henks-side-chick', HenksSideChick)
