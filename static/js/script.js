const card = data => `
<div
  class="rounded-lg shadow-lg hover:shadow-xl hover:shadow-green-light bg-green-medium py-4 px-3 hover:scale-105 transition-all"
>
  <div class="max-w-[250px] min-h-[150px] text-center text-brokenwhite">
    <div
      class="w-[250px] h-[150px] rounded bg-cover bg-center"
      style="
        background-image: url(${data.fields.image_url});
      "
    ></div>
    <p class="font-bold text-orange-light mt-4 truncate">${
      data.fields.title
    }</p>
    <p class="font-bold">
      <span class="text-orange-light">Rp</span> ${data.fields.money_accumulated}
      <span class="text-orange-light font-normal text-xs">terkumpul</span>
    </p>
    <div class="h-3 bg-brokenwhite rounded-full mt-4">
      <div class="h-3 bg-orange-medium rounded-full w-[${
        (100 * data.fields.money_accumulated) / data.fields.money_needed
      }%]"></div>
    </div>
    <div class="relative flex justify-center items-center  mt-4">
      <div class="grow">
        <button
          class="text-orange-dark font-bold bg-orange-light py-2 px-3 rounded hover:scale-110 hover:shadow-md transition-all hover:shadow-brokenwhite/50"
          onclick="location.href='/donation/${data.pk}'"
        >
          Donasi
        </button>
      </div>
      ${
        data.fields.curr_role == 1
          ? `<div class="absolute right-0 hover:scale-110 text-orange-light cursor-pointer flex-none" id="saved-${
              data.pk
            }" onclick="updateSaved(${data.pk})">
          ${
            data.fields.is_saved
              ? `<svg
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
              </svg>`
              : `<svg
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
              </svg>`
          }
        </div>`
          : ``
      }
    </div>
  </div>
</div>`;

const updateSaved = id => {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  $.ajax({
    url: "saved/",
    type: "POST",
    headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
    mode: "same-origin", // Do not send CSRF token to another domain.
    data: {
      id: id,
    },
    success: data => {
      if (data.status == 200) {
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
          url: "saved/delete/" + id,
          type: "DELETE",
          headers: { "X-CSRFToken": csrftoken }, // give CSRF token to the header
          mode: "same-origin", // Do not send CSRF token to another domain.
          success: data => {
            if (data.status == 200) {
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
