const username = $(location).attr("pathname").split("/")[2];

const updateSaved = id => {
  // delete saved and delete card
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  $.ajax({
    url: `/saved/delete/${id}/`,
    type: "DELETE",
    headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
    mode: "same-origin", // Do not send CSRF token to another domain.
    success: response => {
      if (response.status == 200) $(`#card-${id}`).remove();
      if ($("#saved-card").children().length == 0) {
        $("#no-donation").html(
          "<div class='text-center text-green-dark text-[15px] md:text-[20px] '>Maaf, anda tidak menyimpan donasi apapun.</div>"
        );
      }
    },
  });
};

$(document).ready(() => {
  const render = data => {
    const cards = data.map(card).join("");
    $("#saved-card").html(cards);
  };

  $.ajax({
    url: "/saved/json/" + username + "/",
    type: "GET",
    success: data => {
      if (data.length == 0) {
        $("#no-donation").html(
          "<div class='text-center text-green-dark text-[15px] md:text-[20px] '>Maaf, anda tidak menyimpan donasi apapun.</div>"
        );
      } else {
        render(data);
      }
    },
    error: error => {
      console.log(error);
    },
  });
});
