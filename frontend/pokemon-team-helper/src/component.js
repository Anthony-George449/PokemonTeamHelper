import React from 'react';

class ClassComponent extends React.Component {

  render() {
    return <h1>A man named {this.props.firstName}</h1>
  }
}

function FuncComponent(arg1, arg2){
  return(
    <h1 style={{ backgroundColor: 'green' }}>A man named {arg1} {arg2}</h1>
  );
}

export {ClassComponent, FuncComponent};