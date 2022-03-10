document.write(`
    <div class="col-md-4">
        <div class="card">
            <div class="card-header fs-5 py-2">Dashboard</div>
            <div class="list-group list-group-flush accordion accordion-flush" id="sidebarAccordion">
                <div class="list-group-item accordion-item">
                    <h2 class="accordion-header" id="sidebarItemOne">
                        <button class="accordion-button collapsed w-100" type="button"
                            data-bs-toggle="collapse" data-bs-target="#collapseItemOne" aria-expanded="true"
                            aria-controls="collapseItemOne">
                            Profile
                        </button>
                    </h2>
                    <div id="collapseItemOne" class="accordion-collapse collapse"
                        aria-labelledby="sidebarItemOne" data-bs-parent="#sidebarAccordion">
                        <div class="accordion-body">
                            <ul class="list-group list-group-flush">
                                <a class="list-group-item" href="{% url 'main-profile'  %}">View Profile</a>
                                <a class="list-group-item" href="{% url 'profile-update'  %}">Edit Profile</a>
                        </div>
                    </div>
                </div>
                <div class="list-group-item accordion-item">
                    <h2 class="accordion-header" id="sidebarItemTwo">
                        <button class="accordion-button collapsed w-100" type="button"
                            data-bs-toggle="collapse" data-bs-target="#collapseItemTwo" aria-expanded="true"
                            aria-controls="collapseItemTwo">
                            Appointments
                        </button>
                    </h2>
                    <div id="collapseItemTwo" class="accordion-collapse collapse"
                        aria-labelledby="sidebarItemTwo" data-bs-parent="#sidebarAccordion">
                        <div class="accordion-body">
                            <ul class="list-group list-group-flush">
                                {% if user.user_type__name == "Super User" %}
                                    <a class="list-group-item" href="{% url 'superadmin-appointments' %}">View all Appointments</a>
                                    <a class="list-group-item" href="{% url 'superadmin-newappointments' %}">Create New</a>
                                {% elif user.user_type__name == "Super User" %}
                                    <a class="list-group-item" href="{% url 'staff-appointments' %}">View all Appointments</a>
                                    <a class="list-group-item" href="{% url 'superadmin-newappointments' %}">Create New</a>
                                {% else %}
                                    <a class="list-group-item" href="{% url 'user-appointments' %}">View all Appointments</a>
                                    <a class="list-group-item" href="{% url 'superadmin-newappointments' %}">Create New</a>
                                 {% endif %}


                        </div>
                    </div>
                </div>
                <div class="list-group-item accordion-item">
                    <h2 class="accordion-header" id="sidebarItemTwo">
                        <a class="accordion-button collapsed w-100 fw-normal" style="text-decoration:none;" href="">Services</a>
                    </h2>
                </div>
            </div>
        </div>
    </div>
`);
