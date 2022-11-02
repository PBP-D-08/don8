$(document).ready(() => {
    const template = data => `
        
        <div
        class=" rounded-2xl bg-cover bg-center w-full h-[200px] md:h-[300px]"
        style="
        background-image: url('${data.fields.image_url}');
        ">
        </div>
        <div class="flex flex-col gap-4">
            <p class="font-bold text-orange-light text-2xl md:text-3xl mt-6 text-center">${data.fields.title
        }</p>
            <p class="font-bold flex flex-col items-center mb-1">
                <span>
                    <span class="text-orange-light text-xl">Rp</span>
                    <span id="money-accumulated" class="text-xl">${data.fields.money_accumulated
            .toLocaleString("en-US")
            .replaceAll(",", ".")}</span>
                    <span class="text-orange-light font-normal text-lg"> / </span>
                    <span class="text-xl">${data.fields.money_needed
            .toLocaleString("en-US")
            .replaceAll(",", ".")}</span>
                    <span class="text-orange-light font-normal text-lg">terkumpul</span>
                </span>
            </p>
        </div>
        <div class="h-3 bg-brokenwhite rounded-full mt-2">
            <div id = "progress_bar" class="h-3 bg-orange-medium rounded-full w-[${data.fields.money_accumulated / data.fields.money_needed > 1
            ? 100
            : (100 * data.fields.money_accumulated) /
            data.fields.money_needed
        }%]">
            </div>
        </div>
        <div class="mt-3 flex flex-col items-center">
            <span>
                <span class="text-orange-light text-lg">Berakhir pada</span>
                <span class="font-bold">${data.fields.date_expired}</span>
            </span>
        </div>
        <div class="flex flex-col items-center mt-1">
            <button
                class="text-orange-dark font-bold bg-orange-light py-2 px-3 mt-4 rounded hover:scale-110 hover:shadow-md transition-all hover:shadow-brokenwhite/50"
                id="make-donation-button"                   
            >
                Donasi
            </button>
        </div>
    `;

    const template2 = data => `
        <p class="font-bold text-orange-light text-2xl md:text-3xl">Deskripsi</p>
        <p class="text-lg mt-5">${data.fields.description}</p>
    `;

    const template3 = data => `
        <div class="flex flex-row items-center" style="justify-content:space-between">
            <p class="font-bold text-orange-light text-xl md:text-2xl">${data[0].fields.username}</p>
            <button class="text-orange-dark font-bold bg-orange-light py-2 px-3 rounded hover:scale-110 hover:shadow-md transition-all hover:shadow-brokenwhite/50">
                <a href=${data["link"]}>Kunjungi Profil</a>
            </button>
        </div>
    `;
    const template4 = data => `
        <div class="col-2 flex flex-row items-center">
            <div class="text-orange-light text-lg w-[100%] flex flex-col items-start">Terakhir melakukan donasi:</div>
            <div class="font-bold w-[100%] flex flex-col items-center" id="last-donation-time">${data}</div>
        </div>
    `;

    const render_donation = data => {
        $("#donation-main").html(template(data));
        $("#donation-description").html(template2(data));
    };

    const render_organization = data => {
        data["link"] = "{% url 'profile/org:organizations_profile' 0 %}".replace("0", data["donation"].fields.user.toString())
        $("#organization-profile").html(template3(data));
    };

    const render_last_donation = data => {
        $("#last-donation").html(template4(data));
    }

    const id = $(location).attr("pathname").split("/")[2];

    $.ajax({
        url: `/donation/json-donation/${id}/`,
        type: "GET",
        success: donation => {
            render_donation(donation[0]);

            $.ajax({
                url: `/donation/json-organization/${donation[0].fields.user}/`,
                type: "GET",
                success: organization => {
                    organization["donation"] = donation[0]
                    render_organization(organization);

                    $.ajax({
                        url: `/donation/get-last-donation/${id}/`,
                        type: "GET",
                        success: last_donation => {

                            if (last_donation["time"] == "-") {
                                render_last_donation(last_donation["time"]);

                            } else {
                                render_last_donation(last_donation["time"]);
                            }

                        },
                        error: err => {
                            console.log(err);
                        },
                    });

                },
                error: err => {
                    console.log(err);
                },
            });
        },
        error: err => {
            console.log(err);
        },
    });

    const openDonationModal = e => {
        $("#make-donation-modal").removeClass("hidden");
    };

    const closeDonationModal = e => {
        $("#make-donation-modal").addClass("hidden");
    };

    const openUnauthorizedModal = e => {
        $("#unauthorized-modal").removeClass("hidden");
    };

    const closeUnauthorizedModal = e => {
        $("#unauthorized-modal").addClass("hidden");
    };

    const openNoMoneyModal = e => {
        $("#no-money-modal").removeClass("hidden");
    };

    const closeNoMoneyModal = e => {
        $("#no-money-modal").addClass("hidden");
    };

    const openExpiredModal = e => {
        $("#expired-modal").removeClass("hidden");
    };

    const closeExpiredModal = e => {
        $("#expired-modal").addClass("hidden");
    };

    $("body").on("click", "#unauthorized-button", function () {
        closeUnauthorizedModal();
    });

    $("body").on("click", "#no-money-button", function () {
        closeNoMoneyModal();
    });

    $("body").on("click", "#expired-button", function () {
        closeExpiredModal();
    });

    $("body").on("click", "#make-donation-button", function () {
        $.ajax({
            url: `/donation/check-user/`,
            type: "GET",
            success: user => {
                if (user["pengguna"]) {
                    $.ajax({
                        url: `/donation/json-donation/${id}/`,
                        type: "GET",
                        success: donation => {
                            $.ajax({
                                url: `/donation/get-current-date/`,
                                type: "GET",
                                success: date => {
                                    const date_expired =
                                        donation[0].fields.date_expired.split("-");
                                    const current_date = date["current_date"].split("-");

                                    if (
                                        date_expired[0] < current_date[0] ||
                                        (date_expired[0] == current_date[0] &&
                                            date_expired[1] < current_date[1]) ||
                                        (date_expired[0] == current_date[0] &&
                                            date_expired[1] == current_date[1] &&
                                            date_expired[2] <= current_date[2])
                                    ) {
                                        openExpiredModal();
                                    } else {
                                        openDonationModal();
                                    }
                                },
                                error: err => {
                                    console.log(err);
                                },
                            });
                        },
                        error: err => {
                            console.log(err);
                        },
                    });
                } else {
                    openUnauthorizedModal();
                }
            },
            error: err => {
                console.log(err);
            },
        });
    });

    $("#close-icon").click(closeDonationModal);
    $("body").on("submit", "#make-donation-form", function (e) {
        e.preventDefault();

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader(
                    "X-CSRFToken",
                    jQuery("[name=csrfmiddlewaretoken]").val()
                );
            },
        });

        $.ajax({
            type: "POST",
            url: "{% url 'donation_app:make_donation' 0 %}".replace("0", id),
            data: {
                amount_of_donation: $("#id_amount_of_donation").val(),
            },
            success: function (response) {
                $("#make-donation-form").trigger("reset");
                closeDonationModal();

                document.getElementById("money-accumulated").innerHTML =
                    response["data"].money_accumulated
                        .toLocaleString("en-US")
                        .replaceAll(",", ".");

                var progress =
                    response["data"].money_accumulated / response["data"].money_needed > 1
                        ? 100
                        : (100 * response["data"].money_accumulated) / response["data"].money_needed;
                $("#progress_bar").attr(
                    "class",
                    `h-3 bg-orange-medium rounded-full w-[${progress}%]`
                );

                document.getElementById("last-donation-time").innerHTML =
                    response["time"];

                if (response["data"]["message"] == "Not enough money") {
                    openNoMoneyModal();
                }
            },
            error: err => {
                console.log(err);
            },
        });
    });
});