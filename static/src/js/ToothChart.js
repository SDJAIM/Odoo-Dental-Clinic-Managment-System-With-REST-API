odoo.define('dental_clinic.PatientAppointmentToothChart', function(require) {
    'use strict';
    const { Component } = owl;
    const { useState } = owl.hooks;
    const { useListener } = require('web.custom_hooks');
    const FormRenderer = require("web.FormRenderer");
    const { ComponentWrapper } = require("web.OwlCompatibility");

    class PatientAppointmentToothChart extends Component {
        constructor() {
            super(...arguments);
            this.handlers = [];
            useListener('click', this.updateChart);
        }
        
        async mounted() {
            const polygons = this.el.querySelectorAll("polygon, path");
            const toothNumberElements = this.el.querySelectorAll(".tooth_number_class");
            const toothNumbers = Array.from(toothNumberElements).map(el => el.textContent);
            
            for (const element of polygons) {
                element.classList.remove("marked");
                if (toothNumbers.includes(element.id)) {
                    element.classList.add("marked");
                }
                
                const handler = (event) => {
                    if (event.currentTarget.classList.contains("marked")) {
                        event.currentTarget.classList.remove("marked");
                        event.currentTarget.classList.add("unmarked");
                    } else {
                        event.currentTarget.classList.add("marked");
                        event.currentTarget.classList.remove("unmarked");
                    }
                };
                
                element.addEventListener('click', handler);
                this.handlers.push({element, handler});
            }
        }
        
        willUnmount() {
            for (const {element, handler} of this.handlers) {
                element.removeEventListener('click', handler);
            }
            this.handlers = [];
        }
        
        async updateChart() {
            const polygons = this.el.querySelectorAll("polygon, path");
            const toothNumbers = Array.from(this.el.querySelectorAll(".tooth_number_class"))
                .map(el => el.textContent);
            
            for (const element of polygons) {
                element.classList.remove("marked");
                if (toothNumbers.includes(element.id)) {
                    element.classList.add("marked");
                }
            }
        }
    }

    FormRenderer.include({
        async _renderView() {
            await this._super(...arguments);
            
            for (const element of this.el.querySelectorAll(".o_toothChart")) {
                this._rpc({
                    model: "dental.procedure.line",
                    method: "read",
                    args: [[this.state.data.count]]
                }).then(data => {
                    (new ComponentWrapper(
                        this, 
                        PatientAppointmentToothChart
                    )).mount(element);
                });
            }
        }
    });

    PatientAppointmentToothChart.template = 'PatientAppointmentFormToothChart';
    return PatientAppointmentToothChart;
});
