const openModal = e => {
  $("#defaultModal").removeClass("hidden");
};

const closeModal = e => {
  $("#defaultModal").addClass("hidden");
};

const updateSaved = id => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  $.ajax({
    url: "/saved/",
    type: "POST",
    headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
    mode: "same-origin", // Do not send CSRF token to another domain.
    data: {
      id: id,
    },
    success: response => {
      if (response.status == 200) {
        $(`#saved-${id}`).html(`
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    class="w-7 h-7"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M6.32 2.577a49.255 49.255 0 0111.36 0c1.497.174 2.57 1.46 2.57 2.93V21a.75.75 0 01-1.085.67L12 18.089l-7.165 3.583A.75.75 0 013.75 21V5.507c0-1.47 1.073-2.756 2.57-2.93z"
                      clip-rule="evenodd"
                    />
                  </svg>
                `);
      } else {
        $.ajax({
          url: `/saved/delete/${id}/`,
          type: "DELETE",
          headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
          mode: "same-origin", // Do not send CSRF token to another domain.
          success: Response => {
            if (Response.status == 200) {
              $(`#saved-${id}`).html(`
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke-width="1.5"
                        stroke="currentColor"
                        class="w-7 h-7"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          d="M17.593 3.322c1.1.128 1.907 1.077 1.907 2.185V21L12 17.25 4.5 21V5.507c0-1.108.806-2.057 1.907-2.185a48.507 48.507 0 0111.186 0z"
                        />
                      </svg>
                    `);
            }
          },
        });
      }
    },
    error: error => {
      console.log(error);
    },
  });
};

$(document).ready(() => {
  $("#create-donation").click(openModal);
  $(".classtutup").click(closeModal);

  const render = data => {
    const cards = data.map(card).join("");
    $("#donations-card").html(cards);
  };

  $.ajax({
    url: "/donation",
    type: "GET",
    success: data => {
      data.sort((a, b) => {
        const dateA = new Date(a.fields.date_expired);
        const dateB = new Date(b.fields.date_expired);
        return dateA - dateB;
      });
      if (data.length == 0) {
        $("#no-donation").html(
          "<div class='text-center text-green-dark text-[15px] md:text-[20px] '>Maaf, saat ini sedang tidak tersedia donasi apapun.</div>"
        );
      } else {
        render(data);
      }
    },
    error: err => {
      console.log(err);
    },
  });
});

$(document).on("submit", "#post-form", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: "/add_ajax_donation/",
    dataType: "json",
    data: {
      title: $("#title").val(),
      description: $("#description").val(),
      date_expired: $("#date_expired").val(),
      image_url: $("#image_url").val(),
      money_needed: $("#money_needed").val(),
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post",
    },
    success: function (data) {
      $("#post-form").trigger("reset");
      closeModal();
      $("#donations-card").prepend(card(data));
      $("#no-donation").empty();
    },
  });
});
