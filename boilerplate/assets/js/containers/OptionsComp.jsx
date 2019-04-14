import * as React from "react";

export default class OptionsComp extends React.Component{
    constructor() {
        super();
        this.state = {
            options: null
        };
    }

    componentDidMount() {
        this.fetchOptions();
    }


    fetchOptions() {
        const URL = "/api/options";

        fetch(URL).then(res => res.json()).then(json => {
            this.setState({ options: json });
        });
    }

    render() {
        const data = this.state;

        if (!data) return <div>Loading</div>;

        return <div>{JSON.stringify(data)}</div>;
    }
}