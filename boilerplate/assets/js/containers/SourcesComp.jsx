import * as React from "react";

export default class SourcesComp extends React.Component{
    constructor() {
        super();
        this.state = {
            sources: null
        };
    }

    componentDidMount() {
        this.fetchSources();
    }


    fetchSources() {
        const URL = "/api/sources";

        fetch(URL).then(res => res.json()).then(json => {
            this.setState({ sources: json });
        });
    }

    render() {
        const data = this.state;

        if (!data) return <div>Loading</div>;

        return <div>{JSON.stringify(data)}</div>;
    }
}